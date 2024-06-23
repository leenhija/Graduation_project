<script>
export default {
  components: {},
};
</script>
<template>
  <div class="nav">
    <div class="navigation">
      <h1
        class="logo"
        @click="$router.push({ name: 'loggedin', reload: true })"
      >
        Rapidly
      </h1>
    </div>
  </div>
  <div class="edditing_team">
    <div class="teams">
      <div class="teamTitle"><p>Meet our Team</p></div>
      <div class="twoCards">
        <div class="card">
          <div class="teamName">Leen Abu Alhija'</div>
          <div class="teamEmail">
            <img src="@/assets/teamIcon.svg" class="linkedinIcon" />
            <div class="memberEmail">
              <img src="@/assets/memberEmailIcon.svg" />
              <p>leenhija171@gmail.com</p>
            </div>
          </div>
        </div>
        <div class="card">
          <div class="teamName">Miran Alshamaly</div>
          <div class="teamEmail">
            <img src="@/assets/teamIcon.svg" class="linkedinIcon" />
            <div class="memberEmail">
              <img src="@/assets/memberEmailIcon.svg" />
              <p>miranrakan@gmail.com</p>
            </div>
          </div>
        </div>
      </div>
      <div class="twoCards">
        <div class="card">
          <div class="teamName">Leen Almanaseer</div>
          <div class="teamEmail">
            <img src="@/assets/teamIcon.svg" class="linkedinIcon" />
            <div class="memberEmail">
              <img src="@/assets/memberEmailIcon.svg" />
              <p>leenn.almanaseer@gmail.com</p>
            </div>
          </div>
        </div>
        <div class="card">
          <div class="teamName">Seba Almahmoud</div>
          <div class="teamEmail">
            <img src="@/assets/teamIcon.svg" class="linkedinIcon" />
            <div class="memberEmail">
              <img src="@/assets/memberEmailIcon.svg" />
              <p>seba.oooaa@gmail.com</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style>
body {
  overflow-x: hidden;
}
.navigation {
  height: 64px;
  display: flex;
  flex-direction: row;
  justify-content: left;
  margin-left: 40px;
}
.navigation .logo {
  font-family: "Twinkle Star", cursive;
  font-size: 50px;
  font-weight: 900;
  color: white;
  border-color: rgb(232, 93, 93);
  cursor: grab;
}
.nav {
  width: 100vw;
  height: 75px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  position: fixed;
  top: 0;
  background-color: #d9d9d9;
  overflow: hidden;
  color: white;
  font-family: "Roboto", sans-serif;
  border-radius: 0px 0px 30px 30px;
  border: none;
  margin-right: 30px;
  margin-left: 0px;
  z-index: 999;
}
.edditing_team {
  width: 100vw;
  height: 900px;
  flex-shrink: 0;
  border-radius: 36px;
  background: #fbfcfe;
  box-shadow: 0px 20px 80px 0px rgba(0, 0, 0, 0.25);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 30px;
}
.teams {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 30px;
  width: 1100px;
  height: 500px;
  margin-top: 100px;
  border-radius: 36px;
  background: #eae9ea;
  padding: 30px;
  box-shadow: 0px 20px 80px 0px rgba(0, 0, 0, 0.25);
}
.teamTitle {
  color: #6362e3;
  font-family: "Montserrat", sans-serif;
  font-size: 30px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
}
.twoCards {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  gap: 30px;
}
.card {
  display: flex;
  flex-direction: row;
  gap: 40px;
  width: 500px;
  height: 176px;
  border-radius: 26px;
  background: #d9d9d9;
  box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25),
    0px 4px 90px 10px rgba(0, 0, 0, 0.25);
  padding: 10px;
}
.teamName {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #616161;
  text-align: center;
  font-family: "Montserrat", sans-serif;
  font-size: 24px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
}
.teamEmail {
  display: flex;
  flex-direction: column;
  width: 264px;
  justify-content: center;
  align-items: center;
  gap: 20px;
  padding: 20px;
}
.linkedinIcon {
  width: 52px;
  height: 52px;
}
.memberEmail {
  display: flex;
  flex-direction: row;
  gap: 20px;
  color: v#5F5F5F;
  font-family: "Montserrat", sans-serif;
  font-size: 15px;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
}
</style>
