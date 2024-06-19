<script setup>
import ImageComponent from "@components/app/ImageComponent.vue";
import axios from "axios";
import {onBeforeMount, reactive} from "vue";
import OrderComponent from "@components/profile/OrderComponent.vue";
import {useRouter} from "vue-router";
import {useStore} from "vuex";
import InfoSectionTemplate from "@templates/profile/InfoSectionTemplate.vue";
import OrdersSectionTemplate from "@templates/profile/OrdersSectionTemplate.vue";
import LoadImageComponent from "@components/profile/LoadImageComponent.vue";

const state = reactive({
	user: {
		login: "",
		firstName: "",
		lastName: "",
		age: "",
		country: "",
		email: "",
		phone: "",
		img: ""
	},
	orders: []
})

const router = useRouter()
const store = useStore()

const fetchUserData = () => {
	axios.get('http://127.0.0.1:8000/users/')
			.then((e) => {
				state.user.id = e.data['id']
				state.user.login = e.data['login']
				state.user.firstName = e.data['first_name']
				state.user.lastName = e.data['last_name']
				state.user.country = e.data['country']
				state.user.age = e.data['age']
				state.user.email = e.data['email']
				state.user.phone = e.data['phone']
				state.user.img = e.data['user_photo']
				const orders = e.data['orders']
				state.orders = []
				for (let el of orders) {
					el.customer = {
						id: el.customer,
						img: state.user.img,
						firstName: state.user.firstName,
						lastName: state.user.lastName,
					}
					state.orders.push(el)
				}
			})
			.catch((e) => {
				router.push({'name': 'signin'})
			})
}

onBeforeMount(() => {
	if (store.state.userToken !== null) {
		fetchUserData()
	} else {
		router.push({'name': 'signin'})
	}

})

</script>

<template>
	<div class="container">
		<div id="header" class="mt-[75px] p-[56px] flex gap-[92px] bg-[#222222] rounded-[10px]">
			<LoadImageComponent :img="state.user.img" :user_id="state.user.id" @refresh="fetchUserData()" />
			<InfoSectionTemplate v-bind="state.user" />
		</div>
		<OrdersSectionTemplate :orders="state.orders" />
	</div>
</template>
