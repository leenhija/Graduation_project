<script setup lang="js">
import AnswerOption from '@/components/answer_option.vue'
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css';
import { toRef } from 'vue';
const props = defineProps({
    question:Object
});

const question = toRef(props,'question');


</script>

<template>
    <div class="question">
        <QuillEditor v-model:content="question.mcq"
                content-type="html"
        />

        <div         :style="{
                    display:'flex',
                    justifyContent:'flex-start',
                    flexDirection:'column',
                    gap:'1rem',
                    marginTop:'1rem',
                }">

      
        <template v-for="item in question.option">
            
            <AnswerOption :optionValue="item" />
        </template>  </div>
    </div>
</template>



<style lang="css" scoped>
        .question{
            padding: 20px;
            border: 1px solid #9f9f9f;
            border-radius: 5px;
        }
</style>