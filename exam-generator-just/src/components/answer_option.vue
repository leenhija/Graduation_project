
<script setup lang="js">
import { toRef } from 'vue';

const props = defineProps({
    optionValue:String
})


const option = toRef(props , 'optionValue')
</script>

<template>
    <div>
        <input v-model="option" type="text" style="padding: 5px;width: 900px;" >
    </div>
</template>


<style lang="scss" scoped>

</style>