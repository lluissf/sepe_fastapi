<template>
  <div class="">
    <h1>Listagem de Produtos</h1>
    <form>
      <input v-model="novo_produto.nome" placeholder="Nome do Produto">
      <input v-model="novo_produto.preco" type="number" placeholder="Preço do Produto">
      <button @click.prevent="adicionarProduto">Adicionar Produto</button>
    </form>
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
import axios from 'axios'
import { ref , reactive} from 'vue'

const produtos = ref([])
const novo_produto = reactive({
  nome: '',
  preco: 0
})

async function buscarProdutos() {
  const response = await axios.get('/produtos');
  produtos.value = response.data;
}

async function adicionarProduto() {
  await axios.post('/produtos/', { ...novo_produto });
  novo_produto.nome = '';
  novo_produto.preco = 0;
}
</script>

<style scoped>
</style>
