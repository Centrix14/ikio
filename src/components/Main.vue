<template>
	<div class="wrapper">
		<!-- Верхнее меню -->
		<div class="header">
			<div class="header-menu">
				<div class="header-menu__item" :key="item" v-for="item in header_menu.menu_list">
					<a href="#" class="item_text"> {{ item }} </a>
				</div>
			</div>
			<div class="header-profile"></div>
		</div>
		<!-- Левое меню -->
		<div class="left-filters">
			<div class="filter-item" :key="index" v-for="index in left_filters.index_list">
				<p class="filter-item__text"> {{ left_filters.items_list[index] }}</p>
				<input type="checkbox" v-bind:value="index">
			</div>
		</div>
		<!-- Карта -->
		<div class="map"></div>
	</div>
</template>

<script>
export default {
	data: () => {
		return {
			left_filters: {
				index_list: [0,1,2,3,4,5],
				items_list: ['Жилой фонд', 'Места ТКО', 'Световые опоры', 'Светофоры', 'Мосты', 'Тротуары'],
			},
			header_menu: {
				menu_list: ['Карта', 'Таблица', 'Реестр']
			}
		}
	}
}
</script>

<style scoped>
body {
	box-sizing: border-box;
}
.wrapper {
	/* display: flex; */
}
.left-filters {
	width: 20%;
	height: 100vh;
	display: inline-block;

	border: 1px solid black;
}
.filter-item {
	height: 70px;
	/* border: 1px solid black; */
	display: flex;
	justify-content: space-between;
	align-items: center;
}
.header {
	height: 68px;
	background-color: #AEAEAE;

	/* border: 1px solid black; */
}
.filter-item__text {
	padding-left: 13px;

	color: #000;
	font-family: Ubuntu;
	font-size: 24px;
	font-style: normal;
	font-weight: 400;
	line-height: normal;
}
input {
	transform:scale(1.6);
	margin-right: 20px;
}
.header-menu__item:first-child {
	margin-left: 305px;
}
.header-menu__item {
	width: 343px;
	height: 68px;
	display: inline-flex;

	border-radius: 10px;
	border: 3px solid #000;
	background: #ECEBEB;

	color: #000;
	font-family: Ubuntu;
	font-size: 24px;
	font-style: normal;
	font-weight: 400;
	line-height: normal;

	align-items: center;
}
.item_text {
	margin-left: 30px;
	text-decoration: none;
	color: #000;
}
</style>