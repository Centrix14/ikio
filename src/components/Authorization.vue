<template>
  <div class="wrapper">
		<div class="title">
			<p>Авторизация</p>
		</div>
		<!-- <hr noshade size="10"> -->
		<div>
			<v-text-field clearable label="Логин" v-model="input_login" variant="outlined" class="input-lable"></v-text-field>
			<v-text-field clearable label="Пароль" v-model="input_password" variant="outlined" class="input-lable"></v-text-field>
		</div>
		<v-btn class="btn" @click="authorization">
			Войти
		</v-btn>
  </div>
</template>

<script>
export default {
	name: "Authorization",
	props: {
		authorization_status: Boolean
	},
	data: () => {
		return {
			input_login: "",
			input_password: "",
			current_login: "fentomi",
			current_password: "12345",
		}
	},
	methods: {
		authorization() {
			if (this.input_login === this.current_login && this.input_password && this.current_password) {
				this.$emit("authoriz_success");
			} 
		}
	}
}
</script>

<style scoped>
@font-face {
  font-weight: 400;
  font-family: Ubuntu;
  src: url("../../fonts/Ubuntu-Light.ttf");
}
body {
	background-color: #ECEBEB;
	font-family: Ubuntu;
}
.wrapper {
	width: 560px;
	height: 427px;
	margin: 20vh auto;
	padding: 43px 65px;

	text-align: center;
	background-color: #FFF;
	box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.45);
}
.title {
	font-weight: bold;
	margin-bottom: 10px;
}
.input-lable {
	margin-top: 30px;
}
.btn {
	background-color: #97B37B;
	width: 156px;
	height: 46px;
	border-radius: 5px;
	box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
}
.input-entry {
	border-radius: 5px;
	background: #ECEBEB;
	box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
}
</style>