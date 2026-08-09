<script setup>
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";
import ToastNotification  from "@/components/ToastNotification.vue"
</script>

<template>
  <div class="container py-3 d-flex flex-column min-vh-100">
    <Navbar />
    <ToastNotification />
    <main class="flex-grow-1 d-flex flex-column">
      <router-view />
    </main>
    <Footer />
  </div>
</template>
