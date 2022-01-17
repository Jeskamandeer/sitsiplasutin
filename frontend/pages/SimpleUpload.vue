<template>
    <div class="container">
        <form @submit.prevent="onSubmit">
            <div class="form-group">
                <input type="file" @change="onFileUpload">
            </div>
            <div class="form-group">
                <input type="text" v-model="name" placeholder="Pöytien lukumäärä:" class="form-control">
            </div>
            <div class="form-group">
                <button class="btn btn-primary btn-block btn-lg">Plaseeraamaan!</button>
            </div>
        </form>
    </div>    
</template>

<script>
import Vue from 'vue'
import axios from "axios";

export default Vue.extend({
  name: 'IndexPage',

  data() {
      return {
         FILE: "",
         name: ''
      };
    },
    methods: {
        onFileUpload (event) {
          this.FILE = event.target.files[0]
        },
        onSubmit() {
          // upload file
          const formData = new FormData()
          formData.append('FILE', this.FILE)
          formData.append('name', this.name)
          axios.post('http://localhost:5000/sitsiplasutin', formData, {
          }).then((res) => {
            console.log(res)
          })
        }  
    }

})
</script>