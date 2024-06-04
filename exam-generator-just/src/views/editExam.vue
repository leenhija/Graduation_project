<template>
<navigationBar></navigationBar>
<div class="exam">
    <textarea type="text" class="textbox" ></textarea>
     <button class="export">Export</button>
</div>
</template>
<script>
import navigationBar from '../components/navigation_bar.vue'
export default{
components:{
navigationBar:navigationBar
}
}
</script>
<style>
.exam{
    width: 100vw;
    height: 900px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 10px;
    margin-top: -40px;
}
 .exam .textbox{
width: 1260px;
height: 550px;
border-radius: 40px;
background: #C6C6D7;
border: none;
padding: 30px;
display: flex;
flex-direction: column;
outline: none;
box-sizing: border-box;
resize: none;
} 
 .textbox:focus{
border:solid 1px #6362E3;
}
.exam .export{
    border-radius: 30px;
background:  #6362E3;
box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
display: inline-flex;
padding: 17px 43px;
justify-content: center;
align-items: center;
border: none;
gap: 10px;
color: var(--Get-started, #FFF);
text-align: center;
font-family: "Roboto",sans-serif;
font-size: 30px;
font-style: normal;
font-weight: 700;
line-height: normal;
}
</style>