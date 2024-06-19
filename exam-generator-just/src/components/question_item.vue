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
       const response=axiosInstance.patch(`/api/questions/${id}`,{
        question:exam.value.question
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
        <QuillEditor v-model:content="exam.question"
                content-type="html"
        />
        <div         :style="{
                    display:'flex',
                    justifyContent:'flex-start',
                    flexDirection:'column',
                    gap:'1rem',
                    marginTop:'1rem',
                }">

      
        <template v-for="item in exam.answers">
            <AnswerOption :optionValue="item" />
        </template> 
     </div>
     <div class="buttons">
        <button class="btn" @click.prevent="save">
            Submit
        </button>
     </div>
    </div>
</template>



<style lang="css" scoped>
        .question{
            padding: 20px;
            border: 1px solid #9f9f9f;
            border-radius: 5px;
        }

        .buttons{
            display: flex;
            justify-content: flex-end;
            align-items: center;
        }

        .btn{
            padding: 10px 2rem;
            background-color: blue;
            color: white;
            outline: none;
            border: none;
            margin-top: 20px;
        }
</style>