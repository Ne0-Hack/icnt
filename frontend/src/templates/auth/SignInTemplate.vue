<script setup>
import AuthAreaComponent from "@components/app/FormAreaComponent.vue";
import InputAuthComponent from "@components/app/InputComponent.vue";
import {reactive} from "vue";
import axios from "axios";
import {useStore} from "vuex";
import {useRouter} from "vue-router";

const store = useStore()
const router = useRouter()


const state = reactive({
	username: "",
	password: "",
	errors: []
})

const signIn = () => {
	state.errors = []
	axios.post(`${import.meta.env.VITE_API_ENDPOINT}/auth/`, {
		"username": state.username,
		"password": state.password
	})
			.then((e) => {
				store.commit('UPDATE_USER_TOKEN', e.data['token'])
				router.push({name: 'profile'})
			})
			.catch((e) => {
				if (e.response) {
					state.errors = e.response.data
				} else {
					state.errors.push({'non_field_errors': ["Ошибка сервера"]})
				}
			})
}

</script>

<template>
	<div class="flex justify-center items-center ">
		<AuthAreaComponent class="w-[450px]"
											 rows="2"
											 submit-text="Войти"
											 flow-col
											 @onSubmit="signIn()">
			<template #title>Авторизация</template>
			<template #body>
				<InputAuthComponent placehloder="Логин"
														:error="state.errors['username']"
														@onInput="val => state.username = val"
				/>
				<InputAuthComponent placehloder="Пароль"
														:error="state.errors['password']"
														@onInput="val => state.password = val"
														type="password"
				/>
			</template>
			<template #error>
					<span v-for="val of state.errors['non_field_errors']">
					{{ val }}
					</span>
			</template>
			<template #footer>

				<div>
					Ещё нет аккаунта?
					<RouterLink to="/auth/signup">Создать</RouterLink>
				</div>
			</template>
		</AuthAreaComponent>
	</div>
</template>