<script setup>
import { ref } from 'vue';
import api from "@/services/api";
import { useRouter } from "vue-router";

const router = useRouter();
const errMsg = ref("");

const role = ref("");
const name = ref("");
const email = ref("");
const password = ref("");
const confirm_password = ref("");

const handleRegister = async () => {
    console.log("Registering as:", role.value, email.value);

    try {
        const resp = await api.post("/auth/register", {
            name: name.value,
            email: email.value,
            password: password.value,
            confirm_password: confirm_password.value,
            role: role.value
        });

        console.log(resp.data);
        router.push("/login");

    } catch (err) {
        console.log(err);
        if (err.response?.data?.errors) {
            const errorsObj = err.response.data.errors;
            const firstErrorKey = Object.keys(errorsObj)[0]; 
            const messageArray = errorsObj[firstErrorKey]; 

            errMsg.value = Array.isArray(messageArray) ? messageArray[0] : messageArray;
        } else {
            errMsg.value = "Registration failed! Please try again.";
        }
    }
};
</script>

<template>
  <div class="d-flex justify-content-center align-items-center flex-grow-1">
    <form class="form" @submit.prevent="handleRegister">
        <div class="title">Create Account<br><span>join as a student or company</span></div>

        <div v-if="errMsg" class="alert-box text-danger bg-danger bg-opacity-25">
          {{ errMsg }}
        </div>

        <select v-model="role" class="input mb-3" style="cursor: pointer;" required>
          <option value="" hidden>Select Your Role</option>
          <option value="student" class="input">Student</option>
          <option value="company" class="input">Company</option>
        </select>

        <input type="name" v-model="name" placeholder="Name" class="input" required>
        <input type="email" v-model="email" placeholder="Email" class="input" autocomplete="email" required>
        <input type="password" v-model="password" placeholder="Password" class="input" autocomplete="new-password" required>
        <input type="password" v-model="confirm_password" placeholder="Confirm Password" class="input" autocomplete="new-password" required>
        
        <button type="submit" class="portal-btn portal-btn-dark">Sign Up →</button>

        <div class="text-center mt-2 w-100">
            <span class="text-muted small">Already have an account? </span>
            <router-link to="/login" class="fw-bold text-decoration-none" style="color: var(--input-focus);">
                Login
            </router-link>
        </div>
    </form>
  </div>
</template>
