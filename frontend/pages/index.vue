<template>
  
  <div class="section">
       <h1>Sitsiplasutin 3000</h1>
       <p>"Better get busy sittin, boi!"</p>
      <simple-upload/>
  </div>
</template>

<script>
import SimpleUpload from './SimpleUpload.vue';

export default {
  name:"App",
  components: { SimpleUpload }
}
</script>


<style>

h1 {
  text-align: center;
  margin-top: 7%;

}

p {
  text-align: center;
  margin-top: 50px;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap');
* {
  box-sizing: border-box;
  margin: 10;
  padding: 10;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

body {
  font-family: 'Poppins', sans-serif;
}
.container {
  max-width: 500px;
  margin: 30px auto;
  overflow: auto;
  min-height: 300px;
  border: 1px solid steelblue;
  padding: 30px;
  border-radius: 5px;
  padding-top: 50px;
}
.btn {
  display: inline-block;
  align-items:center;
  background: #000;
  color: #fff;
  border: none;
  padding: 20px 40px;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  font-size: 15px;
  font-family: inherit;
}
.btn:focus {
  outline: none;
}
.btn:active {
  transform: scale(0.98);
}
.btn-block {
  display: block;
  width: 100%;
}
</style>
