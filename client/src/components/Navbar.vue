<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { authState, navbarState } from "@/store";

const router = useRouter();

navbarState.value.showSearch = true;

const handleSearch = () => {
  router.push({
    query: {
      q: navbarState.value.searchQuery
    }
  });
};

const handleLogout = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    localStorage.removeItem("role");

    localStorage.clear();
    
    authState.value.isLoggedIn = false;
    authState.value.role = "";
    
    router.push("/login");
};

const handleBack = () => {
    if (navbarState.value.backRoute) {
      router.push(navbarState.value.backRoute);
    } else {
      router.back();
    }
};
</script>

<template>
  <div class="">
    <header class="portal-card px-3 py-2 mb-4">
      
      <!-- LANDING PAGE -->
      <div v-if="!authState.isLoggedIn" class="d-flex justify-content-between align-items-center">
        <router-link class="d-inline-flex align-items-center navbar-brand fw-bold fs-5 mb-0" style="color: #323232; text-decoration: none;" to="/">
            <VsxIcon iconName="Home" type="linear" size="20" color="#333" class="me-1" />Placement Portal
        </router-link>
        <div class="d-flex align-items-center gap-2">
            <router-link to="/login" class="portal-btn portal-btn-dark">Login</router-link>
            <router-link to="/register" class="portal-btn portal-btn-primary">Register</router-link>
        </div>
      </div>

      <!-- EDIT PROFILE & LIST PAGES -->
      <div v-else-if="navbarState.showBackBtn">
        
        <!-- Desktop View -->
        <div class="d-none d-md-flex align-items-center gap-2">
            <h3 class="fw-bold mb-0 fs-5">{{ navbarState.title }}</h3>
            <div class="ms-auto d-flex align-items-center gap-2">
                
                <form v-if="navbarState.showSearch" @submit.prevent="handleSearch" class="d-flex mb-0">
                    <input v-model="navbarState.searchQuery" type="text" :placeholder="navbarState.searchPlaceholder || 'Search...'" class="portal-search-input" style="width:260px;" aria-label="Search" />
                    <button class="portal-btn portal-btn-primary" style="border-radius:0 5px 5px 0; height:36px; padding: 0 15px;" type="submit">Search</button>
                </form>

                <button @click="handleBack" class="portal-btn portal-btn-dark text-decoration-none">
                  <VsxIcon iconName="Back" :size="20" type="linear" /> Back
                </button>
            </div>
        </div>

        <!-- Mobile View -->
        <div class="d-flex d-md-none flex-column gap-2">
            <div class="d-flex justify-content-between align-items-center">
                <h3 class="fw-bold mb-0 fs-5">{{ navbarState.title }}</h3>
                <button @click="handleBack" class="portal-btn portal-btn-dark text-decoration-none">
                  <VsxIcon iconName="Back" :size="20" type="linear" />
                </button>
            </div>
            
            <form v-if="navbarState.showSearch" @submit.prevent="handleSearch" class="d-flex w-100">
                <input v-model="navbarState.searchQuery" type="text" :placeholder="navbarState.searchPlaceholder || 'Search...'" class="portal-search-input flex-grow-1" aria-label="Search" />
                <button class="portal-btn portal-btn-primary" style="border-radius:0 5px 5px 0; height:36px; padding: 0 15px;" type="submit">Search</button>
            </form>
        </div>

      </div>
      
      <!-- DASHBOARDS -->
      <div v-else>
        
        <!-- Desktop View -->
        <div class="d-none d-md-flex align-items-center gap-2">
            <h1 class="fs-5 fw-bold mb-0">{{ navbarState.title }}</h1>
            <div class="ms-auto d-flex align-items-center gap-2">
                
                <!-- Dynamic Search -->
                <form v-if="navbarState.showSearch" @submit.prevent="handleSearch" class="d-flex mb-0">
                    <input v-model="navbarState.searchQuery" type="text" :placeholder="navbarState.searchPlaceholder || 'Search...'" class="portal-search-input" style="width:260px;" aria-label="Search" />
                    <button class="portal-btn portal-btn-primary" style="border-radius:0 5px 5px 0; height:36px; padding: 0 15px;" type="submit">Search</button>
                </form>
                
                <!-- Edit Profile Link -->
                <router-link v-if="navbarState.showProfileBtn" :to="navbarState.profileRoute || '/profile'" class="portal-btn portal-btn-dark">
                  <VsxIcon iconName="Profile" :size="20" color="#333" type="linear" />Edit Profile
                </router-link>
                
                <button @click="handleLogout" class="portal-btn portal-btn-danger">
                    <VsxIcon iconName="LogoutCurve" :size="20" type="linear" /> Logout
                </button>
            </div>
        </div>

        <!-- Mobile View -->
        <div class="d-flex d-md-none flex-column gap-2">
            <div class="d-flex justify-content-between align-items-center">
                <h1 class="fs-5 fw-bold mb-0">{{ navbarState.title }}</h1>
                <div class="d-flex gap-2">
                    <router-link v-if="navbarState.showProfileBtn" :to="navbarState.profileRoute || '/profile'" class="portal-btn portal-btn-dark">
                      <VsxIcon iconName="Profile" :size="20" color="#333" type="linear" />
                    </router-link>
                    <button @click="handleLogout" class="portal-btn portal-btn-danger">
                        <VsxIcon iconName="LogoutCurve" :size="20" type="linear" />
                    </button>
                </div>
            </div>
            
            <form v-if="navbarState.showSearch" @submit.prevent="handleSearch" class="d-flex w-100">
                <input v-model="navbarState.searchQuery" type="text" :placeholder="navbarState.searchPlaceholder || 'Search...'" class="portal-search-input flex-grow-1" aria-label="Search" />
                <button class="portal-btn portal-btn-primary" style="border-radius:0 5px 5px 0; height:36px; padding: 0 15px;" type="submit">Search</button>
            </form>
        </div>
      </div>

    </header>
  </div>
</template>
