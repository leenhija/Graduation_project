<script setup lang="js">
import axiosInstance from '@/axios';
import AnswerOption from '@/components/answer_option.vue'
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css';
import axios from 'axios';
import { toRef } from 'vue';
const props = defineProps({
    exam:Object
});
const exam = toRef(props,'exam');
const save=async()=>{
    console.log(exam.value) //question
    const id=exam.value.id;
    console.log(exam.value);
    // console.log(id2);
    const qustionWithoutTags = exam.value.question.replace(/<\/?p>/g, '');
       const response=axiosInstance.patch(`/api/questions/${id}`,{
        question:qustionWithoutTags
   })
exam.value.answers.forEach((answerObj, index) => {
const response2=axiosInstance.patch(`/api/answers/${answerObj.id}`,{
    answer:answerObj.answer
})
});
   console.log(response)
}
</script>

<template>
  <div class="question">
    <QuillEditor v-model:content="exam.question" content-type="html" />
    <div
      :style="{
        display: 'flex',
        justifyContent: 'flex-start',
        flexDirection: 'column',
        gap: '1rem',
        marginTop: '1rem',
      }"
    >
      <template v-for="item in exam.answers">
        <AnswerOption :optionValue="item" />
      </template>
    </div>
    <div class="buttons">
      <button class="btn" @click.prevent="save">Submit</button>
    </div>
  </div>
</template>

<style lang="css" scoped>
.question {
  padding: 20px;
  border: 1px solid #9f9f9f;
  border-radius: 5px;
}

.buttons {
  display: flex;
  justify-content: flex-end;
  align-items: center;
}

.btn {
  color: white;
  outline: none;
  border: none;
  margin-top: 20px;
  display: flex;
  padding: 11px 46px;
  justify-content: center;
  align-items: center;
  gap: 10px;
  border-radius: 40px;
  background: #6362e3;
  box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
  color: #f4f3f4;
  font-family: "Montserrat", sans-serif;
  font-size: 16px;
  font-style: normal;
  font-weight: 600;
  line-height: normal;
}
</style>
