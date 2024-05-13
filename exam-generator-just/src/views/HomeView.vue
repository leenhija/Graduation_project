<template>
<generation_bar></generation_bar>
<get_started></get_started>
<features></features>
<footer_bar></footer_bar>
</template>
<script >
import generation_bar from '../components/generation_bar.vue'
import get_started from '../components/get_started.vue'
import  features  from '../components/features.vue'
import footer_bar from '../components/footer_bar.vue'
export default{
  components:{
   generation_bar:generation_bar,
   get_started:get_started,
   features:features,
   footer_bar:footer_bar
  },
  
  }

</script>

<style>
body{
  overflow-x: hidden;
  margin-bottom: 0px;
}




</style>
