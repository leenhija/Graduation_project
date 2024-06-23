<template>
  <div class="edditing_2">
    <div class="apearance_part1">
      <h4>Privacy Policy</h4>
      <p class="p1">
        Welcome to our website Rapidly. We are committed to protecting your
        privacy. This Privacy Policy explains how we collect, use, disclose, and
        safeguard your information when you visit our website rapidily.com.
      </p>
      <p class="p2">
        We may collect information about you in a variety of ways. The
        information we may collect on the Site includes:
      </p>
      <p class="p3">Personal Data</p>
      <p class="p4">
        Personally identifiable information, such as your name, email address,
        and phone number, and country, that you voluntarily give to us when you
        register with the Site or when you choose to participate in various
        activities related to the Site.
      </p>
      <p class="p5">
        If you access the Site via a google account, we may collect your related
        profile information.
      </p>
    </div>
    <div class="back">
      <button @click="$router.push({ name: 'loggedin', reload: true })">
        Back
      </button>
    </div>
  </div>
</template>
<script>
import router from "@/router";
const jwtToken = localStorage.getItem("token");
export default {
  data() {
    return {};
  },
  methods: {},
};
</script>
<style>
.edditing_2 {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 30px;
  width: 900px;
}
.apearance_part1 {
  width: 900px;
  display: flex;
  flex-direction: column;
  gap: 43px;
  padding-top: 30px;
  padding-left: 70px;
}
.apearance_part1 h4 {
  color: #393939;
  font-family: "Montserrat", sans-serif;
  font-size: 30px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
}

.p1 + .p2 + .p4 + .p5 {
  color: #393939;
  font-family: "Montserrat", sans-serif;
  font-size: 20px;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
}

.apearance_part1 .p3 {
  color: #393939;
  font-family: "Montserrat", sans-serif;
  font-size: 23px;
  font-style: normal;
  font-weight: 600;
  line-height: normal;
}
.back {
  width: 900px;
  display: flex;
  flex-direction: row;
  justify-content: end;
  padding-right: 30px;
}
.back button {
  border-radius: 40px;
  background: #6362e3;
  box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
  display: flex;
  padding: 11px 46px;
  justify-content: center;
  align-items: center;
  gap: 10px;
  color: #f4f3f4;
  font-family: "Roboto", sans-serif;
  font-size: 20px;
  font-style: normal;
  font-weight: 600;
  line-height: normal;
  border: none;
  cursor: grab;
}
</style>
