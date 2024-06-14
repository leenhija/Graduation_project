<script>
import { Editor, EditorContent } from "@tiptap/vue-3";
import StarterKit from "@tiptap/starter-kit";
import axiosInstance from "@/axios";
import navigation_bar from "@/components/navigation_bar.vue";
import QuestionItem from "@/components/question_item.vue";
import { QuillEditor } from "@vueup/vue-quill";
import "@vueup/vue-quill/dist/vue-quill.snow.css";
import { faL } from "@fortawesome/free-solid-svg-icons";

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
      filename:''
    };
  },
  methods: {
    async test() {
      try {
        this.btnLoading = true;
        const formData = new FormData();
        formData.append("file", this.uploadefile);
        formData.append("examMaterial", this.text);
        formData.append("easyMcq", this.easy);
        formData.append("midMcq", this.mid);
        formData.append("hardMcq", this.sendFilharde);
        formData.append("optionNum", this.numOfOPtions);
        const { data } = await axiosInstance.post("/api/exam", formData);
        this.exam = data;
        console.log(data);
      } catch (e) {
        console.log("error", e);
      } finally {
        this.btnLoading = false;
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
    uploadFile(event) {
      this.uploadefile = event.target.files[0];
      this.filename=event.target.files[0].name;
      this.uploaded = true;
    },
    addcontent() {
      document.getElementById("quill").innerHTML = this.newtext;
    },
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
  <navigation_bar></navigation_bar>
  <form class="generation" @submit.prevent="test">
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
        <p class="yourfile" v-show="uploaded">
          uploaded file: {{ filename }}
        </p>
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
          {{ btnLoading ? "Loading..." : "Generate" }}
        </button>
      </div>
    </div>
  </form>
  <div class="container" v-if="exam?.questions">
    <div v-for="data in exam.questions" class="mcq">
      <QuestionItem :exam="data" />
    </div>
  </div>
</template>

<style>
.generation {
  width: 100vw;
  height: 700px;
  display: flex;
  flex-direction: row;
  margin-top: 80px;
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
  max-width: 1200px;
  padding: 1rem;
  margin: auto;
}
</style>
