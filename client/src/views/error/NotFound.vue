<script setup>
import { DotLottieVue } from '@lottiefiles/dotlottie-vue';
</script>

<template>
  <div class="d-flex flex-column align-items-center justify-content-center flex-grow-1 text-center">
    <DotLottieVue
      src="https://lottie.host/eafea6b6-6e96-46b2-9321-917fd2f8d40a/xRBKc8r2gL.lottie"
      autoplay
      loop
      style="height: 500px;"
    />
    
    <router-link to="/" class="portal-btn portal-btn-primary mt-2">← Back to Home</router-link>
  </div>
</template>
