import { defineStore } from "pinia";
import { ref } from "vue";
 
import axiosInstance from '@/axios';

export const userStore = defineStore("user", () => {
  const user = ref();

  const getUser = async () => {
    const { data } = await axiosInstance.get(`/api/auth/me`);
     user.value = data;
  };
  return {
    user,
    getUser,
  };
});
