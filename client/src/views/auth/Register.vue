<script setup>
import { ref } from 'vue';
import api from "@/services/api";
import { useRouter } from "vue-router";
import { alertState } from "@/store"

const router = useRouter();

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

        alertState.value = {
            type:"success",
            message:"Registration successful!"
        }

        router.push("/login");

    } catch (err) {
        let errorMsg = err.response?.data?.error || "Error during Registration. Please try again.";
    
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
};
</script>

<template>
  <div class="d-flex justify-content-center align-items-center flex-grow-1">
    <form class="form" @submit.prevent="handleRegister">
        <div class="title">Create Account<br><span>join as a student or company</span></div>

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
