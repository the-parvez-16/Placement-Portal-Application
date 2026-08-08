<script setup>
import { ref } from "vue";
import { authState } from "@/store";
import { useRouter } from "vue-router";
const router = useRouter();

const handleLogout = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    localStorage.removeItem("role");
    
    authState.value.isLoggedIn = false;
    authState.value.role = "";
    
    router.push("/login");
};
</script>


<template>
  <div class="container mt-3">
    <header class="portal-card px-3 py-2 mb-4 d-flex justify-content-between align-items-center">
        <router-link class="d-inline-flex align-items-center navbar-brand fw-bold fs-5 mb-0" style="color: #323232; text-decoration: none;" to="/">
            <VsxIcon iconName="Home" type="linear" size="20" color="#333" class="me-1" />Placement Portal
        </router-link>
        
        <div class="d-flex align-items-center gap-2">
          <template v-if="!authState.isLoggedIn">
            <router-link to="/login" class="portal-btn portal-btn-dark">Login</router-link>
            <router-link to="/register" class="portal-btn portal-btn-primary">Register</router-link>
          </template>

          <template v-else>
            <router-link to="/dashboard" class="portal-btn portal-btn-primary">Dashboard</router-link>
            <button class="portal-btn portal-btn-danger" @click="handleLogout">Logout</button>
          </template>
        </div>
    </header>
  </div>
</template>
