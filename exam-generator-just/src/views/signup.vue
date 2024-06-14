<template>
  <div class="container">
    <router-link :to="{ name: 'home' }" class="homeRoute">
      <div class="navigation">
        <h1 class="logo">Rapidly</h1>
      </div>
    </router-link>
    <div class="signup_container" id="signup_container">
      <form @submit.prevent="signup">
        <h2 class="title">SIGN UP</h2>
        <div class="signup_line"></div>
        <div class="input-group username-group">
          <input
            type="text"
            id="firstName"
            autocomplete="off"
            placeholder="firstName"
            v-model="firstName"
            required
            @keyup.enter="focusNextInput($event, 'phone')"
            @input="validateUsername"
          />
          <small id="username-error" v-show="username_rules"
            >your user name should consist of at least 6 characters</small
          >
        </div>
        <div class="input-group username-group">
          <input
            type="text"
            id="lastName"
            autocomplete="off"
            placeholder="lastName"
            v-model="lastName"
            required
            @keyup.enter="focusNextInput($event, 'phone')"
            @input="validateUsername"
          />
          <small id="username-error" v-show="username_rules"
            >your user name should consist of at least 6 characters</small
          >
        </div>
        <div class="input-group phone-group">
          <input
            type="tel"
            id="phone"
            autocomplete="off"
            placeholder="Phone Number"
            v-model="phone"
            required
            maxlength="10"
            @input="validatephone"
          />
          <small id="phone-error" v-show="phone_rules"
            >your phone number must start with 0</small
          >
        </div>
        <div class="input-group email-group">
          <input
            type="email"
            id="email"
            autocomplete="off"
            placeholder="Email Address"
            v-model="email"
             required
          />
          <small id="email-error" v-show="email_rules"
            >valid email : user@example.com</small
          >
        </div>
        <div class="input-group password-group">
          <input
            type="password"
            id="password"
            autocomplete="off"
            placeholder="Password"
            v-model="password"
            required
            @input="validatePassword"
            @focus="condition"
          />
          <small class="pass-char" id="pass-char" v-show="show_password_rules"
            >Password should contain:
            <li>
              atleast 8 chacters
              <i
                class="fa-solid fa-check"
                id="8-char"
                v-show="rule_1"
                style="color: #61b143"
              ></i>
            </li>
            <li>
              one lowercase letter<i
                class="fa-solid fa-check"
                id="lowercase"
                v-show="rule_2"
                style="color: #61b143"
              ></i>
            </li>
            <li>
              one uppercase letter<i
                class="fa-solid fa-check"
                id="uppercase"
                v-show="rule_3"
                style="color: #61b143"
              ></i>
            </li>
            <li>
              at least one number<i
                class="fa-solid fa-check"
                id="one-num"
                v-show="rule_4"
                style="color: #61b143"
              ></i>
            </li>
            <li>
              one special character<i
                class="fa-solid fa-check"
                id="special"
                v-show="rule_5"
                style="color: #61b143"
              ></i></li
          ></small>
        </div>
        <button class="getstarted" type="submit" id="signup">
          Get Started
        </button>
        <p class="have_an_account">
          Already have an account?
          <router-link :to="{ name: 'login' }"
            ><button class="loginlink">Login</button></router-link
          >
        </p>
      </form>
    </div>
  </div>
</template>
<script>
import axiosInstance from '@/axios';
 export default{
data(){
  return{
    firstName:'',
    lastName:'',
phone: '',
email:'',
password:'',
has_minimum_lenth: false,
has_number: false,
has_lowercsae: false,
has_uppercase: false,
has_special: false,
show_password_rules:false,
username_rules:false,
email_rules:false,
phone_rules:false,
rule_1:false,
rule_2:false,
rule_3:false,
rule_4:false,
rule_5:false,
  };
},
methods:{
async signup(){
  try {
    console.log("sign up");
        const response = await axiosInstance.post(`api/auth/register`, {
          email: this.email,
          password: this.password,
          firstName: this.firstName,
          lastName: this.lastName,
          phone:this.phone,
        });
        console.log(response);
        // Reset form fields
        // Redirect or show success message
        this.$router.push('/signin');
        this.verify();

      } catch (error) {
console.log(error);
        this.email_rules=true;
        document.getElementById("email").setAttribute("style","border-color: rgb(232, 93, 93)");
        document.getElementById("email-error").innerHTML="this email is alraedy used!";
      }
},
validateEmail() {
    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(this.email)) {
      document.getElementById("email").setAttribute("style","border-color: rgb(76, 207, 76)");
      this.email_rules=false
    } else {
        document.getElementById("email").setAttribute("style","border-color: rgb(232, 93, 93)");
        this.email_rules=true;
    }
    },
    validateUsername(){
      if(this.firstName.length<6){
        document.getElementById("firstName").setAttribute("style","border-color: rgb(232, 93, 93)");
          this.username_rules=true;
      }
      else{
        document.getElementById("firstName").setAttribute("style","border-color: rgb(76, 207, 76)");
        this.username_rules=false;
      }
    },
    validatephone(){
      this.handelphone();
      if(this.phone.length==10 && this.phone.substring(0,1)=='0'){
        document.getElementById("phone").setAttribute("style","border-color: rgb(76, 207, 76)");
        this.phone_rules=false;
      }
      else if(this.phone.length!=10){
        document.getElementById("phone").setAttribute("style","border-color: rgb(232, 93, 93)");
        this.phone_rules=true;
      }
      else if (this.phone.substring(0,1)!='0' && this.phone.length==10){
        document.getElementById("phone").setAttribute("style","border-color: rgb(232, 93, 93)");
        this.phone_rules=true;
      }
    },
    focusNextInput(event, nextInput) {
      // Prevent default behavior of "Enter" key
      event.preventDefault();

      // Focus on the next input field
      this.$refs[nextInput].focus();
    },
    validatePassword(){
            this.has_minimum_lenth = (this.password.length > 8);
            this.has_number    = /\d/.test(this.password);
            this.has_lowercase = /[a-z]/.test(this.password);
            this.has_uppercase = /[A-Z]/.test(this.password);
            this.has_special   = /[!@#\$%\^\&*\)\(+=._-]/.test(this.password);
            if(this.has_minimum_lenth){
            this.rule_1=true;
            }
            if(this.has_lowercase){
            this.rule_2=true;
            }
            if(this.has_uppercase){
            this.rule_3=true;
            }
            if(this.has_number){
            this.rule_4=true;
            }
            if(this.has_special){
            this.rule_5=true;
            }
            if(this.has_minimum_lenth==true && this.has_number==true && this.has_lowercase==true && this.has_uppercase==true && this.has_special==true){
              document.getElementById("password").setAttribute("style","border-color: rgb(76, 207, 76)");
              document.getElementById("signup_container").setAttribute("style","height:500px");
              this.show_password_rules=false;
            }
            else{
              document.getElementById("password").setAttribute("style","border-color: rgb(232, 93, 93)");

            }
        },
        condition(){
          this.show_password_rules=true;
          document.getElementById("signup_container").setAttribute("style","height:600px");
        },
        handelphone(){
        this.phone=this.phone.replace(/\D/g,'');
        },
        async verify(){
          const verify= await axiosInstance.post(`send`,{
          email:this.email
        })
        }
}
};
</script>
<style>
.container {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #e9eced;
  background-position: center bottom;
  background-repeat: no-repeat;
  background-size: cover;
}
.navigation {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: left;
  margin-left: 0px;
}
.homeRoute {
  text-decoration: none;
}
.navigation .logo {
  font-family: "Twinkle Star", cursive;
  font-size: 40px;
  font-weight: 400;
  font-style: normal;
  color: white;
  font-weight: bold;
  padding: 20px;
}

.signup_container {
  width: 479px;
  height: 600px;
  gap: 5px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f4f3f4;
  margin: auto;
  margin-top: -10px;
  border-radius: 35px;
  filter: drop-shadow(15px 15px 8px rgba(0, 0, 0, 0.25));
}
.signup_container .title {
  padding-top: 40px;
  font-family: "Outfit", sans-serif;
  font-size: 30px;
  font-weight: 500;
  font-style: normal;
  margin-top: -30px;
  margin-bottom: 30px;
  color: #4b4b4b;
  -webkit-text-stroke-width: 1;
  -webkit-text-stroke-color: #4b4b4b;
  font-size: 30px;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
}
.signup_line {
  width: 41px;
  height: 5px;
  background: #6362e3;
  margin-top: -40px;
}
.signup_container form {
  margin-top: 40px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}
.signup_container form .input-group {
  position: relative;
}
.signup_container form .input-group label {
  position: absolute;
  top: 50%;
  left: 10px;
  color: #a7a7a7;
  transform: translateY(-50%);
  font-size: 16px;
  transition: 0.5s;
}
.signup_container form input {
  width: 320px;
  height: 30px;
  border-radius: 40px;
  border: 1px solid #a7a7a7;
  padding: 10px;
  padding-left: 17px;
  margin-bottom: 10px;
  box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
  font-family: "Roboto", sans-serif;
  transition: border-color 0.5s;
}
.signup_container form input:focus {
  outline: none;
  border-color: #6362e3;
}

.password-group {
  display: flex;
  flex-direction: column;
}
.pass-char {
  margin-left: 20px;
  width: 200px;
  color: #a7a7a7;
  font-family: "Roboto", sans-serif;
}
li {
  list-style: none;
  display: inline-block;
}
.username-group {
  display: flex;
  flex-direction: column;
}
.username-group small {
  color: #a7a7a7;
  margin-left: 20px;
  font-family: "Roboto", sans-serif;
  /* visibility: hidden; */
}
.email-group {
  display: flex;
  flex-direction: column;
}
.email-group small {
  color: #a7a7a7;
  margin-left: 20px;
  font-family: "Roboto", sans-serif;
  /* visibility: hidden; */
}
.phone-group {
  display: flex;
  flex-direction: column;
}
.phone-group small {
  color: #a7a7a7;
  margin-left: 20px;
  font-family: "Roboto", sans-serif;
  /* visibility: hidden; */
}
.fa-check {
  color: #61b143;
  padding-left: 5px;
}
.signup_container form input:focus {
  border-color: #6362e3;
}
.signup_container form .have_an_account {
  color: rgb(0, 0, 0, 0.52);
  font-size: 16px;
  font-weight: 400;
  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  font-family: "Roboto", sans-serif;
}
.signup_container form .have_an_account .loginlink {
  color: #6362e3;
  background-color: #f4f3f4;
  border-color: transparent transparent transparent transparent;
  cursor: grab;
  font-size: 16px;
}
.signup_container form .getstarted {
  width: 320px;
  height: 45px;
  flex-shrink: 0;
  border-radius: 40px;
  background: #6362e3;
  border-color: transparent;
  box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
  color: white;
  font-family: Roboto, sans-serif;
  font-size: 16px;
  font-weight: 600;
}

.signup_container form button:hover {
  cursor: grab;
}
.hr-lines {
  position: relative;
  width: 304.084px;
  max-width: 500px;
  margin: 20px auto;
  text-align: center;
  color: rgba(0, 0, 0, 0.52);
  font-family: Hannari, sans-serif;
  font-size: 14px;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
}

.hr-lines:before {
  content: " ";
  height: 1px;
  width: 130px;
  background: rgba(0, 0, 0, 0.52);
  display: block;
  position: absolute;
  top: 50%;
  left: 0px;
}

.hr-lines:after {
  content: " ";
  height: 1px;
  width: 130px;
  background: rgba(0, 0, 0, 0.52);
  display: block;
  position: absolute;
  top: 50%;
  right: 0px;
}
.signup_container .with_google {
  display: flex;
  flex-direction: row;
  justify-content: center;
  width: 240.159px;
  height: 28.195px;
  color: rgba(0, 0, 0, 0.52);
  text-align: center;
  font-family: Hannari, sans-serif;
  font-size: 16px;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  margin-top: 10px;
}
.signup_container .with_google img {
  width: 25px;
  height: 25px;
  margin-right: 10px;
  margin-top: -2px;
}
@media only screen and (max-width: 600px) {
  .signup_container {
    width: 346px;
    height: 472px;
  }
  .navigation .logo {
    font-size: 26px;
    margin-bottom: 50px;
  }
  .navigation {
    justify-content: center;
  }
  .signup_container form input {
    width: 263px;
    height: 20px;
  }
  .signup_container form .getstarted {
    width: 216.15px;
  }
}
@media only screen and (min-width: 600px) {
  .signup_container {
    width: 346px;
    height: 472px;
  }
  .navigation .logo {
    font-size: 26px;
    margin-bottom: 50px;
  }
  .navigation {
    justify-content: center;
  }
  .signup_container form input {
    width: 263px;
    height: 20px;
  }
  .signup_container form .getstarted {
    width: 216.15px;
  }
}
@media only screen and (min-width: 768px) {
  .signup_container {
    width: 346px;
    height: 550px;
  }
  .navigation .logo {
    font-size: 45px;
    margin-bottom: 0px;
  }
  .navigation {
    justify-content: left;
  }
}
@media only screen and (min-width: 992px) {
  .signup_container {
    width: 479px;
    height: 550px;
  }
  .navigation .logo {
    font-size: 50px;
    margin-bottom: 0px;
  }
  .signup_container form input {
    width: 320px;
    height: 30px;
  }
  .getstarted {
    width: 320px;
    height: 45px;
  }
}
</style>
