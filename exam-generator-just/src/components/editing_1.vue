<template>
  <form class="edditing_1">
    <div class="profile_part1">
      <h4>Profile</h4>
      <p>Change your profile settings</p>
    </div>
    <div class="profile_part2">
      <div class="profile_part2_a">
        <div class="input_box">
          <p class="edit">USERNAME</p>
          <p>{{ origin_username }}</p>
        </div>
        <div class="input_box">
          <p>EMAIL</p>
          <p>{{ email }}</p>
        </div>
        <div class="input_box">
          <p class="edit">PHONE NUMBER</p>
          <p>{{ origin_phonenumber  }}</p>
        </div>
      </div>
      <div class="profile_part2_b">
        
        
      </div>
    </div>
    <div class="line"></div>
    <div class="profile_part3">
    </div>
  </form>
</template>
<script setup>
import { faL } from "@fortawesome/free-solid-svg-icons";
 const store = userStore();
import { ref,onMounted } from 'vue';
import { userStore } from "@/stores/user";
 const email = ref("");
const username = ref("");
const phoneNumber = ref("");
const country = ref("");
const headline = ref("");
const origin_username = ref("");
const origin_phonenumber = ref("");
const changes = ref(false);
const disable1 = ref(true);
const edit_country = ref(false);
const disable2 = ref(false);
const edit_headline = ref(false);
const disable3 = ref(false);
const edit_phonenumber = ref(false);
const edit_username = ref(false);
const disable4 = ref(false);
const show_country = ref(true);
const show_headline = ref(true);
const user_country = ref("");
const user_headline = ref("");
 onMounted(()=>{
    print_userEmail()
 })
async function print_userEmail() {
    email.value =userStore().user?.email;
  origin_username.value =userStore().user?.firstName;
  origin_phonenumber.value =userStore().user?.phone;

}






 
</script>
<style>
.edditing_1 {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 30px;
  width: 900px;
}
.profile_part1 {
  width: 900px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding-top: 30px;
  padding-left: 70px;
}
.profile_part1 h4 {
  color: #393939;
  font-family: "Montserrat", sans-serif;
  font-size: 30px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
}
.profile_part1 p {
  color: #393939;
  font-family: "Montserrat", sans-serif;
  font-size: 15px;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
}
.profile_part2 {
  width: 900px;
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  padding: 30px;
  gap: 200px;
  padding-left: 100px;
}
.line {
  width: 830.002px;
  height: 1px;
  background: #393939;
}
.profile_part2 p {
  color: #393939;
  font-family: "Montserrat", sans-serif;
  font-size: 15px;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
}
.profile_part2 .profile_part2_a {
  display: flex;
  flex-direction: column;
  gap: 30px;
}
.profile_part2 .profile_part2_b {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.profile_part2 .input_box {
  display: flex;
  flex-direction: column;
  gap: 5px;
}
input {
  padding: 5px;
}
.profile_part2 .normal {
  border-radius: 10px;
  background: #c6c6d7;
  width: 212px;
  height: 37px;
  flex-shrink: 0;
  outline: none;
}
.profile_part2 .normal:focus {
  border: solid 1px #6362e3;
}
.profile_part2 .special {
  border-radius: 10px;
  background: #c6c6d7;
  width: 212px;
  height: 145px;
  flex-shrink: 0;
  outline: none;
  padding: 10px;
  resize: none;
}
.profile_part2 .special:focus {
  border: solid 1px #6362e3;
}

.profile_part3 {
  width: 900px;
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  padding-right: 70px;
}
.profile_part3 .save {
  border-radius: 20px;
  background: #6362e3;
  box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
  width: 176px;
  height: 51px;
  flex-shrink: 0;
  border: none;
  color: #f4f3f4;
  text-align: center;
  font-family: "Roboto", sans-serif;
  font-size: 16px;
  font-style: normal;
  font-weight: 800;
  line-height: normal;
}
.changes {
  width: 900px;
  height: 10px;
  background-color: #eae9ea;
  color: #6362e3;
  font-size: 16px;
  font-family: "Roboto", sans-serif;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: flex-start;
  padding-left: 30px;
  gap: 5px;
}
.edit {
  display: flex;
  width: 222px;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}
.edit button {
  background: #eae9ea;
  /* box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); */
  border-radius: 10px;
  flex-shrink: 0;
  border: none;
  color: #393939;
  text-align: center;
  font-family: "Roboto", sans-serif;
  font-style: normal;
  font-weight: 800;
  line-height: normal;
  padding: 5px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  gap: 3px;
}
</style>
