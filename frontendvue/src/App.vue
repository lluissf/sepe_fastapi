<template>
  <div class="">
    <h1>Listagem de Produtos</h1>
    <hr>
    <button @click="buscarProdutos">Buscar Produtos</button>
    <hr>
    <ul v-if="produtos.length"> 
      <li v-for="produto in produtos" :key="produto.id">
        {{ produto.nome }} - R$ {{ produto.preco }}
      </li>
    </ul>
  </div>
</template>
<script setup>
import axios from '@/plugins/api.js'
import { ref } from 'vue'

const produtos = ref([])

async function buscarProdutos() {
  const response = await axios.get('/produtos');
  produtos.value = response.data;
}
</script>

<style scoped>
</style>
