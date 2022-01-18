<template>
  <div>
  <div class="container">
    <form @submit.prevent="onSubmit">
      <div class="form-group">
        <input type="file" @change="onFileUpload" />
      </div>
      <div class="form-group">
        <input
          type="text"
          v-model="form.table_sizes"
          placeholder="Pöytien koot:"
          class="form-control"
        />
      </div>
      <div class="form-group">
        <button class="btn btn-primary btn-block btn-lg">Plaseeraamaan!</button>
      </div>
    </form>
  </div>
  <div class="d-flex justify-content-around">
      <table class="table m-5 align-self-start w-25"  v-for="(table, i) in shuffled_tables" :key="i">
      <thead>
        <tr>
          <th scope="col"> # </th>
          <th scope="col">Pöytä</th>
          <th scope="col">{{ i }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, i) in table" :key="i">
          <td>{{ (i + 1) * 2 }}</td>
          <td>{{ row[0] }}</td>
          <td>{{ row[1] }}</td>
        </tr>
      </tbody>
    </table>
  </div>
  <div class="d-flex justify-content-around m-5">
    <button @click="csvExport">Tunge CSVeehen</button>
  </div>
  </div>
</template>

<script>
import Vue from "vue";
import axios from "axios";

export default Vue.extend({
  name: "IndexPage",

  data() {
    return {
      sitsers_csv: "",
      form: {
        table_sizes: "",
      },
      shuffled_tables: "",
    };
  },
  methods: {
    csvExport() {
      let csv = "";
      this.shuffled_tables.forEach((table, index) => {
              csv += "Poyta " + index + ";\n"
              table.forEach((row) => {
                csv += row.join(';');
                csv += "\n";
        });
        csv += "\n"
      });

      const anchor = document.createElement('a');
      anchor.href = 'data:text/csv;charset=utf-8,' + encodeURIComponent(csv);
      anchor.target = '_blank';
      anchor.download = 'plaseeraukset.csv';
      anchor.click();
    },
    onFileUpload(event) {
      this.sitsers_csv = event.target.files[0];
    },
    onSubmit() {
      // upload file
      const formData = new FormData();
      formData.append("sitsers_csv", this.sitsers_csv);
      formData.append("json", JSON.stringify(this.form));

      axios({
        url: "http://localhost:5000/sitsiplasutin",
        data: formData,
        method: "POST",
      }).then((res) => {
        this.shuffled_tables = res.data;
      });
    },
  },
});
</script>