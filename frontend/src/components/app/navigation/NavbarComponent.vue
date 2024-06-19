<script setup>
	import Logo from "@images/logo_light.svg"
	import ImageComponent from "@components/app/ImageComponent.vue";
	import {useStore} from "vuex";
	import {useRouter} from "vue-router";

	const store = useStore()
	const router = useRouter()

	const logout = () => {
		store.commit("UPDATE_USER_TOKEN", '')
		router.push({name: 'signin'})
	}
</script>

<template>
	<div class="container">
		<div class="flex items-center gap-[10px] justify-between py-[24px] select-none">
			<router-link :to="{name: 'main'}">
				<ImageComponent width="124px" height="28px" :img="Logo" />
			</router-link>
			<ul class="nav-list ">
				<router-link custom :to="{name: 'main'}" v-slot="{navigate, isActive}" >
					<li @click="navigate" :class="{'active': isActive}">Главная</li>
				</router-link>
				<router-link custom :to="{name: 'works'}" v-slot="{navigate, isActive}" >
					<li @click="navigate" :class="{'active': isActive}">Портфолио</li>
				</router-link>
				<router-link custom :to="{name: 'order_create'}" v-slot="{navigate, isActive}" >
					<li @click="navigate" :class="{'active': isActive}">Оформить заказ</li>
				</router-link>
				<router-link custom :to="{name: 'profile'}" v-slot="{navigate, isActive}" >
					<li @click="navigate" :class="{'active': isActive}">Профиль</li>
				</router-link>
			</ul>
			<button v-if="store.state.userToken !== null" @click="logout()">Выход</button>
			<router-link  v-else :to="{name: 'signin'}">
				<button>Вход</button>
			</router-link>
		</div>
	</div>
</template>

<style>
	.nav-list {
		@apply bg-light flex text-dark gap-[16px] rounded-full px-[5px] py-[2.5px] ;
	}
	.nav-list > li {
		@apply py-[12px] px-[16px] rounded-full cursor-pointer;
	}
	.nav-list > li.active {
		@apply bg-dark text-light;
	}
</style>