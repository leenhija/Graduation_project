<template>
<div>
    <button @click="test()">test</button>
    {{ data }}
</div>
</template>

<script>
import axios from 'axios';
export default{
data(){
    return{
        data:''
    }
},
mounted(){
},
methods:{
    async test(){
  try{ const response=await axios.post('http://127.0.0.1:5000/generate-exam',{
    "material":"Animals are important for the environment and even our lives.",
    "mcqNum":5,
    "optionNum": 5,
    "difficulty":"easy"
    ,headers: {
                    Accept: 'application/json',
                    'Content-Type': 'application/json',
                }
   })
   console.log(response);
   this.data=response.data;
  }catch{
   console.log('error lolo');
   }
  }
}
}
</script>
<style>
</style>