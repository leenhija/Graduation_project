
<script setup lang="js">
import { toRef } from 'vue';


const props = defineProps({
    optionValue:Object
})

const answerItem = toRef(props,'optionValue')
</script>

<template>
    <div class="answer">
        <div class="answer-check"
            :class="{
                'active':answerItem.isCorrect
            }"
        >
        </div>
        <input v-model="answerItem.answer" type="text" class="answer-input">
    </div>
</template>


<style lang="scss" scoped>
    .answer{
        display: flex;
        justify-content: flex-start;
        gap: .5rem;
        &-check{
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background-color:#e2e2e2;
            border:1px solid #e3e3e3;

            &.active{
                background-color: blue;
            }
        }
        &-input{
            padding: .35rem 1rem;
            line-height: 1.3;
            font-size: 14px;
            width: 100%;
        }
    }
</style>