<script setup>
import AuthAreaComponent from "@components/app/FormAreaComponent.vue";
import InputAuthComponent from "@components/app/InputComponent.vue";
import {reactive} from "vue";
import axios from "axios";
import {useStore} from "vuex";
import {useRouter} from "vue-router";
import SelectComponent from "@components/app/SelectComponent.vue";

const store = useStore()
const router = useRouter()


const state = reactive({
	login: "",
	first_name: "",
	last_name: "",
	phone: "",
	email: "",
	password: "",
	country: 0,
	errors: []
})

const signUp = () => {
	state.errors = []
	axios.post(`${import.meta.env.VITE_API_ENDPOINT}/users/`, {
		"login": state.login,
		"first_name": state.first_name,
		"last_name": state.last_name,
		"password": state.password,
		"phone": state.phone,
		"email": state.email,
		"country": state.country,
		"age": state.age
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
	<div class="flex justify-center items-center">
		<AuthAreaComponent class="w-[875px]"
											 rows="4"
											 cols="2"
											 submit-text="Зарегистрироваться"
											 flow-col
											 @onSubmit="signUp()">
			<template #title>Регистрация</template>
			<template #body>
				<InputAuthComponent placehloder="Логин"
														:error="state.errors['login']"
														@onInput="val => state.login = val"
														name="login"
				/>
				<InputAuthComponent placehloder="Пароль"
														:error="state.errors['password']"
														@onInput="val => state.password = val"
														type="password"
														name="password"
				/>
				<InputAuthComponent placehloder="Имя"
														:error="state.errors['first_name']"
														@onInput="val => state.first_name = val"
														name="first_name"
				/>
				<InputAuthComponent placehloder="Фамилия"
														:error="state.errors['last_name']"
														@onInput="val => state.last_name = val"
														name="last_name"
				/>
				<InputAuthComponent placehloder="Возраст"
														:error="state.errors['age']"
														@onInput="val => state.age = val"
														type="number"
														name="age"
				/>
				<SelectComponent placehloder="Страна"
												 :options="[{id: 0, title: 'Россия'}, {id: 1, title: 'Казахстан'}, {id: 2, title: 'Беларусь'}]"
												 opt-id="id"
												 opt-name="title"
												 :error="state.errors['country']"
												 @onInput="val => state.country = val"
												 name="country"
				/>
				<InputAuthComponent placehloder="Почта"
														:error="state.errors['email']"
														@onInput="val => state.email = val"
														type="email"
														name="email"
				/>
				<InputAuthComponent placehloder="Телефон"
														:error="state.errors['phone']"
														@onInput="val => state.phone = val"
														type="phone"
														name="phone"
				/>
			</template>
			<template #error>
					<span v-for="val of state.errors['non_field_errors']">
					{{ val }}
					</span>
			</template>
			<template #footer>
				<div class="text-danger">
					<span v-for="val of state.errors['non_field_errors']">
					{{ val }}
					</span>
				</div>
				<div>
					Уже есть аккаунт?
					<RouterLink to="/auth/signin">Войти</RouterLink>
				</div>
			</template>
		</AuthAreaComponent>
	</div>
</template>