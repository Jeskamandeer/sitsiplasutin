from urllib import response
import pandas as pd
import numpy as np
from io import StringIO

miesten_nimet = pd.read_csv("./datafiles/miesten_nimet.csv", sep=";")
naisten_nimet = pd.read_csv("./datafiles/naisten_nimet.csv", sep=";")

def sovinistinen_algoritmi(sitsers_df):

    sukupuoli_column = []
    
    for i in sitsers_df.values.tolist():
        enimi, *snimi = i[0].split()

        m_maara = 0
        n_maara = 0 
        
        if enimi in miesten_nimet["Etunimi"].values:
            maara = miesten_nimet.loc[miesten_nimet['Etunimi'] == enimi]
            m_maara = maara["Lukumäärä"].values[0]
        
        if enimi in naisten_nimet['Etunimi'].values:
            maara = naisten_nimet.loc[naisten_nimet['Etunimi'] == enimi]
            n_maara = maara["Lukumäärä"].values[0]

        if m_maara > n_maara:
            sukupuoli_column.append(1)
        else:
            sukupuoli_column.append(0)
        
            
    sitsers_df["Sukupuoli"] = sukupuoli_column
    
    return sitsers_df


def table_shuffler(miehet, naiset, ylijaavat):
    shuffled = pd.DataFrame()
    
    for i in range (0, len(naiset)):
        if i % 2:
            shuffled = shuffled.append(miehet.iloc[i], ignore_index=True)
            shuffled = shuffled.append(naiset.iloc[i], ignore_index=True)
        else:
            shuffled = shuffled.append(naiset.iloc[i], ignore_index=True)
            shuffled = shuffled.append(miehet.iloc[i], ignore_index=True)

    if (len(ylijaavat) == 0): return shuffled
    
    for i in range (0, len(ylijaavat)):
        rand_idx = np.random.randint(0, len(ylijaavat))

        shuffled.loc[rand_idx + 0.5] = ylijaavat.iloc[i]
        shuffled = shuffled.sort_index().reset_index(drop=True)
        
    return shuffled


def get_excess_people(miehet, naiset):
    m_miehet = len(miehet)
    m_naiset = len(naiset)


    erotus = abs(m_miehet - m_naiset)

    if m_miehet > m_naiset:
        return miehet[m_miehet - erotus:]
    if m_miehet < m_naiset:
        return naiset[m_naiset - erotus:]
    else:
        return []
    

def table_generator(pituus, np_table):
    return np_table.reshape(pituus, 2)
    

def write_excel(filled_tables):
    data = StringIO()

    for i in range(0, len(filled_tables)):
        pd.DataFrame(filled_tables[i]).to_csv(data,
                                                    index=False, 
                                                    header=[f"Poyta {i}", ""],
                                                    sep=";"
                                                    )
        data.write("\r\n")
        
    return data


def create_tables(poydat, sitsers="./datafiles/sample.xlsx", shuffle_limit=10):

    df = pd.read_excel(sitsers)
    
    # Picks both genders into their own table and shuffles them
    df = sovinistinen_algoritmi(df)
    
    miehet = df.loc[df['Sukupuoli'] == 1]
    naiset = df.loc[df['Sukupuoli'] == 0]
    
    # Shuffles attendees by set number of times
    for i in range(1, shuffle_limit):
        miehet = miehet.sample(frac=1).reset_index(drop=True)
        naiset = naiset.sample(frac=1).reset_index(drop=True)
    
    # Checks if there are more males or females in attendees, returns array of people that dont fit normally 
    ylijaavat = get_excess_people(miehet, naiset)
    if (ylijaavat == 0):
        return response
    # TODO possible indexer out-of-bounds error

    # Merges two DF's into single list with right order
    sorted_df = table_shuffler(miehet, naiset, ylijaavat)
    
    sorted_df = sorted_df.drop("Sukupuoli", axis=1)

    # Turn DF into Numpy for easier usage
    np_table = sorted_df.to_numpy()
    filled_tables = []

    for i in range(0, len(poydat)):
        # Fills each table into their max amount based on one side lenght
        table_length = int(poydat[i] / 2)
        max_table_size = poydat[i]

        # Adds the filled table to list and removes used sitsers from the list
        filled_tables.append(table_generator(table_length, np_table[:max_table_size, :]))
        np_table = np_table[max_table_size:]
        
    
    return filled_tables

