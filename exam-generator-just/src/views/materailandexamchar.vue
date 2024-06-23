<script>
import { Editor, EditorContent } from "@tiptap/vue-3";
import StarterKit from "@tiptap/starter-kit";
import axiosInstance from "@/axios";
import navigation_bar from "@/components/navigation_bar.vue";
import QuestionItem from "@/components/question_item.vue";
import { QuillEditor } from "@vueup/vue-quill";
import "@vueup/vue-quill/dist/vue-quill.snow.css";
import { useRouter } from 'vue-router';
export default {
  components: {
    navigation_bar: navigation_bar,
    QuillEditor,
    EditorContent,
    QuestionItem,
  },
  data() {
    return {
      numOfOPtions: "2",
      choosed: false,
      easy: 0,
      mid: 0,
      hard: 0,
      uploadefile: "",
      uploaded: false,
      sendFile: "",
      text: "",
      exam: null,
      newtext: "",
      editor: null,
      btnLoading: false,
      filename: "",
      showlink: false,
      fileUrl: "",
      fileName: "",
      downloadUrl: "",
      numOfShuffle:0,
      exported:false,
      showExportButton1:true,
      showExportButton2:false,
      showExportBox:false,
      export_sentence:false
    };
  },
  methods: {
    async generateExam() {
      try {
        this.btnLoading = true;
        console.log(this.uploadfile);
        const formData = new FormData();
        formData.append("file", this.uploadefile);
        formData.append("examMaterial", this.text);
        formData.append("easyMcq", this.easy);
        formData.append("midMcq", this.mid);
        formData.append("hardMcq", this.hard);
        formData.append("optionNum", this.numOfOPtions);
        const { data } = await axiosInstance.post("/api/exam", 
          formData
        );
        this.exam = data;
        this.export_sentence=true;
        this.showExportBox=true;
      } catch (e) {
        console.log("error", e);
      } finally {
        this.btnLoading = false;
        const targetElement = document.getElementById("container");
        if (targetElement) {
          targetElement.scrollIntoView({ behavior: "smooth" });
        }
      }
    },

    async Export() {
      this.exported=true;
      try {
        const { file } = await axiosInstance.post("/api/export", {
          ExamID: this.exam.id,
        });
        // this.$router.go();
        console.log("worked");
      } catch {
        console.log(err);
      }
    },
    async shuffle() {
      try {
        console.log(this.exam.id);
        console.log(this.numOfShuffle);
        const examID=this.exam.id;
        const {data }= await axiosInstance.post(`/api/exam/ShuffleExam`, {
         ExamID:this.exam.id,
         numOfShuffle:this.numOfShuffle
        });
        this.exported=true;
      } catch {
        console.log(err);
      }
    },
    maximize1() {
      this.easy += 1;
    },
    minimize1() {
      if (this.easy > 0) this.easy -= 1;
    },
    maximize2() {
      this.mid += 1;
    },
    minimize2() {
      if (this.easy > 0) this.mid -= 1;
    },
    maximize3() {
      this.hard += 1;
    },
    minimize3() {
      if (this.easy > 0) this.hard -= 1;
    },
    maximize4(){
      this.numOfShuffle+=1;
     if(this.numOfShuffle>0){
      this.showExportButton1=false;
      this.showExportButton2=true;
      document.getElementById('export_buttons').setAttribute("style","margin-right:-840px");
     }
    },
    minimize4(){
      this.numOfShuffle-=1;
       if(this.numOfShuffle==0){
        this.showExportButton1=true;
      this.showExportButton2=false;
      document.getElementById('export_buttons').setAttribute("style","margin-left:-10px");

       }
    },
    uploadFile(event) {
      this.uploadefile = event.target.files[0];
      console.log(this.uploadefile);
      this.filename = event.target.files[0].name;
      this.uploaded = true;
    },
    addcontent() {
      document.getElementById("quill").innerHTML = this.newtext;
    },
    regenerate(){
      this.$router.push({name:'materailandexamchar'});
    }
  },
  mounted() {
    this.editor = new Editor({
      content: `<p>${this.exam}</p>`,
      extensions: [StarterKit],
    });
   
  },
};
</script>

<template>
  <navigation_bar class="navi"></navigation_bar>
  <form class="generation" @submit.prevent="generateExam" id="generateID">
    <div class="material">
      <div class="uploadFile">
        <p class="uploadtext">Upload file now</p>
        <input
          type="file"
          name="file"
          id="file"
          class="inputfile"
          @change="uploadFile"
        />
        <label for="file">+</label>
        <p class="yourfile" v-show="uploaded">uploaded file: {{ filename }}</p>
        <div class="orline">
          <div class="line_before"></div>
          <p class="or">or</p>
          <div class="line_after"></div>
        </div>
      </div>
      <div class="writeText">
        <textarea
          type="text"
          v-model="text"
          placeholder="Type here..."
          class="textbox"
          :disabled="uploaded"
        ></textarea>
      </div>
    </div>
    <div class="examchar">
      <div class="diificulty">
        <div class="char_title">
          <h4>Difficulty</h4>
          <p>You can choose multiple level of difficulty</p>
        </div>
        <div class="dificulty_level">
          <div class="choices">
            <label class="easy">Easy</label>
            <p class="plus" @click="maximize1()">+</p>
            <input class="levels" v-model="easy" type="number" />
            <p class="minus" @click="minimize1()">-</p>
          </div>
          <div class="choices">
            <label class="mid">Mid</label>
            <p class="plus" @click="maximize2()">+</p>
            <input class="levels" v-model="mid" type="number" />
            <p class="minus" @click="minimize2()">-</p>
          </div>
          <div class="choices">
            <label class="hard">Hard</label>
            <p class="plus" @click="maximize3()">+</p>
            <input class="levels" v-model="hard" type="number" />
            <p class="minus" @click="minimize3()">-</p>
          </div>
        </div>
      </div>
      <div class="number_of_options">
        <div class="char_title">
          <h4>Number of options</h4>
        </div>
        <div class="range">
          <input
            class="range_slider"
            type="range"
            min="2"
            max="6"
            v-model="numOfOPtions"
          />
        </div>
        <ul class="range_values">
          <li>2</li>
          <li>3</li>
          <li>4</li>
          <li>5</li>
          <li>6</li>
        </ul>
      </div>

      <div class="generate_button_step2">
        <button :disabled="btnLoading">
          {{ btnLoading ? "Generating..." : "Generate" }}
        </button>
      </div>
    </div>
  </form>
  <div class="container" v-if="exam?.questions" id="container">
    <div v-for="data in exam.questions" class="mcq">
      <QuestionItem :exam="data" />
    </div>
  </div>
  <div class="export_sentence" v-show="export_sentence">
    <p class="e1">Master Your Exam!</p>
    <p class="e2">Export with Answers, Shuffle Questions, Get New Forms</p>
  </div>
  <div class="export_box" v-show="showExportBox">
    <div class="export_container">
      <div class="shuffle_regenrate">
      <div class="shuffle_box">
        <div class="shuffle_p">
          <p class="shuffle_title">Shuffled Exam</p>
          <p class="shuffle_dec">Select desired quantity</p>
        </div>
     <div class="shuffle_plus_minus">
      <div class="choices">
            <p class="plus" @click="maximize4()">+</p>
            <input class="levels" v-model="numOfShuffle" type="number" />
            <p class="minus" @click="minimize4()">-</p>
          </div>
     </div>
    </div>
    <div class="regenerate_box">
      <div class="regenerate_p">
        <p class="regenerate_title">New Form?</p>
        <p class="regenerate_dec">Regenerate exam for new form!</p>
      </div>
      <button class="regenerate_button" ><a href="#generateID">Regenerate</a></button>
    </div>
    </div>
  <div class="export_buttons" id="export_buttons">
    <button @click="Export" class="export" v-show="showExportButton1" id="export1">Export</button>
    <button @click="shuffle" class="shuffle_button" v-show="showExportButton2" id="export2">Export</button>
  </div>
  <p v-show="exported" class="exported">Exam Exported successfully</p>


    </div>
  

  </div>
</template>

<style>
.navi{
  z-index: 999;
}
.generation {
  width: 100vw;
  height: 700px;
  display: flex;
  flex-direction: row;
  margin-top: 60px;
  justify-content: center;
  gap: 100px;
  background: #f4f3f4;
  padding-top: 30px;
}

.generation .material {
  width: 660px;
  height: 569px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.uploadFile {
  width: 430px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 20px;
}

.uploadFile .uploadtext {
  color: #5f5f5f;
  text-align: center;
  font-family: "Montserrat", sans-serif;
  font-size: 32px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
}

.yourfile {
  color: #5f5f5f;
  text-align: center;
  font-family: "Montserrat", sans-serif;
  font-size: 14px;
  font-family: 700;
}

.uploadFile .orline {
  width: 413px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  gap: 5px;
}

.uploadFile .orline .line_before {
  width: 200px;
  height: 2px;
  background-color: rgba(0, 0, 0, 0.52);
}

.uploadFile .orline .line_after {
  width: 200px;
  height: 2px;
  background-color: rgba(0, 0, 0, 0.52);
}

.uploadFile .orline .or {
  color: #616161;
  font-family: "Montserrat", sans-serif;
  font-size: 14px;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
}

.generation .writeText {
  width: 660px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.generation .writeText .textbox {
  width: 655px;
  height: 379px;
  border-radius: 40px;
  background: #d9d9d9;
  border: none;
  padding: 30px;
  display: flex;
  flex-direction: column;
  outline: none;
  box-sizing: border-box;
  resize: none;
}

.generation .writeText .textbox::-webkit-scrollbar {
  width: 15px;
  height: 200px;
  margin-right: -80px;
}

.generation .writeText .textbox::-webkit-scrollbar-track {
  background-color: #f4f3f4;
  margin-top: 7px;
  border: solid 1px #6362e3;
  border-radius: 20px;
}

.generation .writeText .textbox::-webkit-scrollbar-thumb {
  background: #c6c6d7;
  border-radius: 200px;
}

.generation .writeText .textbox::-webkit-scrollbar-thumb:hover {
  background: #949292;
}

.generation .writeText .textbox:focus {
  border: solid 1px #6362e3;
}

.generation .examchar {
  border-radius: 40px;
  background: #c6c6d7;
  width: 450px;
  height: 520px;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
  gap: 40px;
  padding-top: 40px;
  padding-left: 50px;
}

.inputfile {
  width: 0.1px;
  height: 0.1px;
  opacity: 0;
  overflow: hidden;
  position: absolute;
  z-index: -1;
}

.inputfile + label {
  font-size: 64px;
  font-weight: bold;
  color: white;
  width: 40px;
  height: 40px;
  background-color: #6362e3;
  padding: 10px;
  border-radius: 50px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  cursor: grab;
}

/* .inputfile:focus + label,
.inputfile + label:hover {
} */
.number_of_options {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}

.number_of_options .range {
  accent-color: #6362e3;
}

.number_of_options .range .range_slider {
  width: 270px;
  height: 20px;
}

.number_of_options .range_values {
  list-style: none;
  display: flex;
  flex-direction: row;
  width: 270px;
  justify-content: space-between;
}

.number_of_options .range_values li {
  color: #ffff;
  text-align: center;
  font-family: "Montserrat", sans-serif;
  font-size: 16px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
}

.char_title {
  width: 270px;
  display: flex;
  flex-direction: column;
  align-items: start;
  margin-bottom: 20px;
}

.char_title h4 {
  color: #5f5f5f;
  text-align: center;
  font-family: "Montserrat", sans-serif;
  font-size: 24px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
}

.char_title p {
  color: #5f5f5f;
  text-align: center;
  font-family: "Montserrat", sans-serif;
  font-size: 12px;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
}

.dificulty {
  width: 150px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}

.dificulty_level {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.dificulty_level .choices {
  width: 180px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  gap: 10px;
  box-shadow: 0px 4px 90px 5px rgba(0, 0, 0, 0.25);
  background-color: #eaeaea;
  padding: 10px;
  border-radius: 30px;
}
.export_container{
  width: 900px;
  height: 350px;
  padding: 30px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #D9D9D9;
  border-radius: 20px;
}
.shuffle_regenrate{
  display:flex;
  flex-direction: row;
  gap: 100px;
  margin-left: -200px;
  margin-top: 50px;
}
.shuffle_box{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
  gap:60px;
  
}
.shuffle_box .shuffle_title{
  color: #393939;
  font-family: "Montserrat", sans-serif;
  font-size: 30px;
font-style: normal;
font-weight: 700;
line-height: normal;
}
.shuffle_box .shuffle_dec{
  color: #393939;
  font-family: "Montserrat", sans-serif;
font-size: 15px;
font-style: normal;
font-weight: 400;
line-height: normal;
}
.shuffle_box .choices{
  width: 150px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  gap: 20px;
  box-shadow: 0px 4px 90px 5px rgba(0, 0, 0, 0.25);
  background-color: #eaeaea;
  padding: 10px;
  border-radius: 30px;
}
.shuffle_box .levels{
  width: 30px;
  border: none;
  border-radius: 30px;
  padding: 10px;
  text-align: center;
  background-color: #eaeaea;
}
.shuffle_plus_minus{
  display:flex;
 flex-direction: column;
}
.regenerate_box{
  display: flex;
  flex-direction: column;
  align-items: start;
  justify-content: center;
  gap:60px;
height:200px;
}
.regenerate_box .regenerate_p{
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: start;
  gap:10px;
  margin-top: -80px;
}
.shuffle_p{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
  margin-top: -70px;
  gap:10px;
}
.regenerate_box .regenerate_title{
  color:  #393939;
  font-family: "Montserrat", sans-serif;font-size: 30px;
font-style: normal;
font-weight: 700;
line-height: normal;
}
.regenerate_box .regenerate_dec{
  color:  #393939;
  font-family: "Montserrat", sans-serif;font-size: 30px;
font-size: 15px;
font-style: normal;
font-weight: 400;
line-height: normal;
}
.regenerate_box .regenerate_button{
  border-radius: 30px;
background: #FFD863;
box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25), 0px 4px 90px 5px rgba(0, 0, 0, 0.25);
display: flex;
width: 196px;
height: 59px;

justify-content: center;
align-items: center;
gap: 10px;
flex-shrink: 0;
border:none;
color: #424242;
text-align: center;
font-family: "Roboto",sans-serif;
font-size: 20px;
font-style: normal;
font-weight: 700;
line-height: normal;

}
.regenerate_button a{
  text-decoration: none;
  color: #424242;

}
input[type="number"]::-webkit-inner-spin-button {
  -webkit-appearance: none;
}

.levels:focus {
  outline: none;
  border-color: #6362e3;
}

.dificulty_level .easy {
  width: 40px;
  height: 18px;
  background-color: rgb(111, 185, 111);
  color: #f4f3f4;
  text-align: center;
  font-size: 15px;
  font-style: normal;
  font-weight: 600;
  font-family: "Montserrat", sans-serif;
  line-height: normal;
  padding: 6px 15px;
  border-radius: 30px;
}

.dificulty_level .mid {
  width: 40px;
  height: 18px;
  background-color: rgb(240, 228, 101);
  color: black;
  text-align: center;
  font-size: 15px;
  font-style: normal;
  font-weight: 600;
  font-family: "Montserrat", sans-serif;
  line-height: normal;
  padding: 6px 15px;
  border-radius: 30px;
}

.dificulty_level .hard {
  width: 40px;
  height: 18px;
  background-color: rgb(240, 79, 79);
  color: #f4f3f4;
  text-align: center;
  font-size: 15px;
  font-style: normal;
  font-weight: 600;
  font-family: "Montserrat", sans-serif;
  line-height: normal;
  padding: 6px 15px;
  border-radius: 30px;
}

.dificulty_level .levels {
  width: 30px;
  border: none;
  border-radius: 30px;
  padding: 10px;
  text-align: center;
  background-color: #eaeaea;
}

.plus {
  font-size: 20px;
  font-weight: 900;
  cursor: grab;
  user-select: none;
}

.minus {
  font-size: 20px;
  font-weight: 900;
  cursor: grab;
  user-select: none;
  margin-right: 5px;
}

.generate_button_step2 {
  width: 400px;
  display: flex;
  flex-direction: row;
  justify-content: end;
  margin-top: -30px;
  padding-top: 10px;
}

.generate_button_step2 button {
  border-radius: 20px;
  background-color: #6362e3;
  display: inline-flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
  color: #fff;
  text-align: center;
  font-family: "Montserrat", sans-serif;
  font-size: 15px;
  font-weight: 700;
  width: 150px;
  height: 50px;
  line-height: normal;
  display: inline-flex;
  padding: 12px 23px;
  margin-right: -20px;
  border: none;
  cursor: grab;
}

.mcq {
  margin-top: 40px;
}

#quill {
  height: 700px;
}

.container {
  max-width: 100vw;
  padding: 1rem;
  margin: auto;
  background-color: #f4f3f4;
}
.export_box {
  width: 100vw;
  height: 400px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 20px;
  padding-bottom: 40px;
  background-color: #f4f3f4;
  padding-top: 60px;
}
.export {
  color: white;
  outline: none;
  border: none;
  margin-top: 20px;
  padding: 11px 46px;
  border-radius: 40px;
  background: #6362e3;
  box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
  color: #f4f3f4;
  font-family: "Montserrat", sans-serif;
  font-size: 16px;
  font-weight: 600;
  cursor: grab;
}
.exported{
 
  color: rgb(111, 185, 111);
  font-family: "Montserrat", sans-serif;
  font-size: 16px;
  margin-left: -40px;
  margin-top: 20px;
  font-weight: 500;
}
.shuffle_button{
  color: white;
  outline: none;
  border: none;
  margin-top: 20px;
  padding: 11px 46px;
  border-radius: 40px;
  background: #6362e3;
  box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
  color: #f4f3f4;
  font-family: "Montserrat", sans-serif;
  font-size: 16px;
  font-weight: 600;
  margin-left:-147px;
  cursor: grab;
}
.export_buttons{
margin-right: -700px;
}
.export_sentence{
  width: 100vw;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 30px;
  background-color: #f4f3f4;
  height: 92px;
  padding: 30px;

}
.export_sentence .e1{
  color:  #393939;
text-align: center;
font-family: "Montserrat", sans-serif;
font-size: 40px;
font-style: normal;
font-weight: 700;
line-height: normal;
}
.export_sentence .e2{
  color:  #393939;
text-align: center;
font-family: "Montserrat", sans-serif;
font-size: 24px;
font-style: normal;
font-weight: 500;
line-height: normal;
}
</style>
