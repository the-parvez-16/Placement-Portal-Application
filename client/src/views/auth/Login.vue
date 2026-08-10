<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import api from "@/services/api";
import { authState, alertState } from "@/store";

const email = ref("");
const password = ref("");

const router = useRouter();

const handleLogin = async () => {
    try {
        const resp = await api.post("/auth/login", {
            email: email.value,
            password: password.value
        });

        const access_token = resp.data.access_token;
        const refresh_token = resp.data.refresh_token;
        localStorage.setItem("access_token", access_token);
        localStorage.setItem("refresh_token", refresh_token);

        const base64Url = access_token.split('.')[1];
        const payload = JSON.parse(atob(base64Url));
        let userRole = payload.role;
        if(userRole === "special_power : sudo"){
            userRole = "sudo";
        }
        localStorage.setItem("role", userRole);

        authState.value.isLoggedIn = true;
        authState.value.role = userRole;

        alertState.value = {
            type:"success",
            message:"Logged in successfully!"
        }

        router.push("/dashboard");

    } catch (err) {
        let errorMsg = err.response?.data?.error || "Error during login. Please try again.";
    
        if (typeof errorMsg === 'object') {
            const firstField = Object.keys(errorMsg)[0];
            const specificError = errorMsg[firstField][0];
            const capitalizedField = firstField.charAt(0).toUpperCase() + firstField.slice(1);
            errorMsg = `${capitalizedField}: ${specificError}`;
        }
        alertState.value = {
            type: "danger",
            message: errorMsg
        };
    }
}
</script>

<template>
  <div class="d-flex justify-content-center align-items-center flex-grow-1">
      
      <form class="form" @submit.prevent="handleLogin">
          <div class="title">Welcome,<br><span>sign in to continue</span></div>

          <input type="email" v-model="email" placeholder="Email" class="input" autocomplete="email" required>
          <input type="password" v-model="password" placeholder="Password" class="input" autocomplete="current-password" required>
          
          <button type="submit" class="portal-btn portal-btn-dark">Sign In →</button>

          <div class="text-center mt-2 w-100">
              <span class="text-muted small">Don't have an account? </span>
              <router-link to="/register" class="fw-bold text-decoration-none" style="color: var(--input-focus);">
                  Register
              </router-link>
          </div>
      </form>
  </div>
</template>

<style>
@import '@/assets/auth.css';
</style>
