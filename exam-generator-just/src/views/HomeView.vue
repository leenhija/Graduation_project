<template>
<generation_bar></generation_bar>
<get_started></get_started>
<About_us></About_us>
<features></features>
<ContactUs></ContactUs>
<footer_bar></footer_bar>
</template>
<script >
import generation_bar from '../components/generation_bar.vue'
import get_started from '../components/get_started.vue'
import  features  from '../components/features.vue'
import footer_bar from '../components/footer_bar.vue'
import About_us from '../components/About_us.vue'
import ContactUs from '@/components/contactUs.vue'

export default{
  components:{
   generation_bar:generation_bar,
   get_started:get_started,
   features:features,
   footer_bar:footer_bar,
   About_us:About_us,
   ContactUs:ContactUs

  },
  
  }

</script>

<style>
body{
  overflow-x: hidden;
  margin-bottom: 0px;
}

::-webkit-scrollbar{
  width: 15px;

}
::-webkit-scrollbar-track {
  background-color:#F4F3F4;
}
::-webkit-scrollbar-thumb {
  background: #D9D9D9;
  border-radius: 20px;
}
::-webkit-scrollbar-thumb:hover {
  background: #949292;
}
</style>
