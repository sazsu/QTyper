from PyQt6.QtCore import Qt


class Config:
	en_words = [
		'the',
		'to',
		'and',
		'of',
		'was',
		'he',
		'you',
		'it',
		'she',
		'that',
		'my',
		'me',
		'on',
		'with',
		'at',
		'as',
		'had',
		'for',
		'but',
		'him',
		'said',
		'be',
		'up',
		'out',
		'look',
		'have',
		'what',
		'not',
		'just',
		'like',
		'they',
		'this',
		'from',
		'all',
		'we',
		'were',
		'back',
		'one',
		'about',
		'know',
		'when',
		'get',
		'then',
		'into',
		'would',
		'there',
		'could',
		'ask',
		'down',
		'time',
		'want',
		'eye',
		'them',
		'over',
		'your',
		'are',
		'been',
		'now',
		'by',
		'think',
		'see',
		'hand',
		'say',
		'how',
		'around',
		'head',
		'did',
		'well',
		'before',
		'off',
		'who',
		'more',
		'even',
		'turn',
		'come',
		'smile',
		'way',
		'really',
		'can',
		'face',
		'other',
		'some',
		'right',
		'their',
		'only',
		'walk',
		'make',
		'got',
		'try',
		'something',
		'room',
		'again',
		'thing',
		'after',
		'still',
		'thought',
		'door',
		'here',
		'too',
		'little',
		'because',
		'why',
		'away',
		'let',
		'take',
		'two',
		'start',
		'good',
		'where',
		'never',
		'through',
		'day',
		'much',
		'tell',
		'girl',
		'feel',
		'oh',
		'call',
		'talk',
		'will',
		'long',
		'than',
		'us',
		'made',
		'friend',
		'knew',
		'open',
		'need',
		'first',
		'which',
		'people',
		'went',
		'sure',
		'seem',
		'stop',
		'voice',
		'very',
		'felt',
		'took',
		'our',
		'pull',
		'laugh',
		'man',
		'okay',
		'close',
		'any',
		'came',
		'told',
		'love',
		'watch',
		'arm',
		'anything',
		'though',
		'put',
		'left',
		'work',
		'guy',
		'hair',
		'next',
		'yeah',
		'while',
		'mean',
		'home',
		'few',
		'saw',
		'place',
		'school',
		'help',
		'wait',
		'late',
		'year',
		'house',
		'happen',
		'last',
		'always',
		'move',
		'old',
		'should',
		'moment',
		'another',
		'behind',
		'side',
		'sound',
		'once',
		'find',
		'toward',
		'ever',
		'nothing',
		'front',
		'mother',
		'name',
		'since',
		'reply',
		'myself',
		'leave',
		'new',
		'car',
		'use',
		'mind',
		'maybe',
	]
	ru_words = [
		'тот',
		'быть',
		'весь',
		'это',
		'как',
		'она',
		'по',
		'но',
		'они',
		'ты',
		'из',
		'мы',
		'за',
		'вы',
		'так',
		'же',
		'от',
		'сказать',
		'этот',
		'который',
		'мочь',
		'человек',
		'один',
		'еще',
		'бы',
		'такой',
		'только',
		'себя',
		'свое',
		'какой',
		'когда',
		'уже',
		'для',
		'вот',
		'кто',
		'да',
		'говорить',
		'год',
		'знать',
		'мой',
		'до',
		'или',
		'если',
		'время',
		'рука',
		'нет',
		'самый',
		'ни',
		'стать',
		'большой',
		'даже',
		'другой',
		'наш',
		'свой',
		'ну',
		'под',
		'где',
		'дело',
		'есть',
		'сам',
		'раз',
		'чтобы',
		'два',
		'там',
		'чем',
		'глаз',
		'жизнь',
		'первый',
		'день',
		'тут',
		'во',
		'ничто',
		'потом',
		'очень',
		'со',
		'хотеть',
		'ли',
		'при',
		'голова',
		'надо',
		'без',
		'видеть',
		'идти',
		'теперь',
		'тоже',
		'стоять',
		'друг',
		'дом',
		'сейчас',
		'можно',
		'после',
		'слово',
		'здесь',
		'думать',
		'место',
		'спросить',
		'через',
		'лицо',
		'что',
		'тогда',
		'ведь',
		'хороший',
		'каждый',
		'новый',
		'жить',
		'должный',
		'смотреть',
		'почему',
		'потому',
		'сторона',
		'просто',
		'нога',
		'сидеть',
		'понять',
		'иметь',
		'конечный',
		'делать',
		'вдруг',
		'над',
		'взять',
		'никто',
		'сделать',
		'дверь',
		'перед',
		'нужный',
		'понимать',
		'казаться',
		'работа',
		'три',
		'ваш',
		'земля',
		'конец',
		'несколько',
		'час',
		'голос',
		'город',
		'последний',
		'пока',
		'хорошо',
		'давать',
		'вода',
		'более',
		'хотя',
		'всегда',
		'второй',
		'куда',
		'пойти',
		'стол',
		'ребенок',
		'увидеть',
		'сила',
		'отец',
		'женщина',
		'машина',
		'случай',
		'ночь',
		'сразу',
		'мир',
		'совсем',
		'остаться',
		'вид',
		'выйти',
		'дать',
		'работать',
		'любить',
		'старый',
		'почти',
		'ряд',
		'оказаться',
		'начало',
		'твой',
		'вопрос',
		'много',
		'война',
		'снова',
		'ответить',
		'между',
		'подумать',
		'опять',
		'белый',
		'деньги',
		'значить',
		'про',
		'лишь',
		'минута',
		'жена',
		'посмотреть',
		'правда',
		'главный',
		'страна',
		'свет',
		'ждать',
		'мать',
		'будто',
		'никогда',
		'товарищ',
		'дорога',
		'однако',
		'лежать',
		'именно',
	]
	keys_to_listen = {
		Qt.Key.Key_A,
		Qt.Key.Key_B,
		Qt.Key.Key_C,
		Qt.Key.Key_D,
		Qt.Key.Key_E,
		Qt.Key.Key_F,
		Qt.Key.Key_G,
		Qt.Key.Key_H,
		Qt.Key.Key_I,
		Qt.Key.Key_J,
		Qt.Key.Key_K,
		Qt.Key.Key_L,
		Qt.Key.Key_M,
		Qt.Key.Key_N,
		Qt.Key.Key_O,
		Qt.Key.Key_P,
		Qt.Key.Key_Q,
		Qt.Key.Key_R,
		Qt.Key.Key_S,
		Qt.Key.Key_T,
		Qt.Key.Key_U,
		Qt.Key.Key_V,
		Qt.Key.Key_W,
		Qt.Key.Key_X,
		Qt.Key.Key_Y,
		Qt.Key.Key_Z,
		Qt.Key.Key_1,
		Qt.Key.Key_2,
		Qt.Key.Key_3,
		Qt.Key.Key_4,
		Qt.Key.Key_5,
		Qt.Key.Key_6,
		Qt.Key.Key_7,
		Qt.Key.Key_8,
		Qt.Key.Key_9,
		Qt.Key.Key_0,
		Qt.Key.Key_Backspace,
		Qt.Key.Key_Space,
	}
	correct_format = '<span class="correct" style="color: #1fc471;">{}</span>'
	wrong_format = '<span class="wrong" style="color: #ff506e;">{}</span>'

	app_light = '''
		* {
			color: #121212;
			background: #f2f2f2;
		}
		QPushButton { border: none; }
		TextArea {
			border: 2px solid black;
		}'''

	app_dark = '''
		* {
			color: #c2c2c2;
			background: #121212;
		}
		QPushButton { border: none; }
		TextArea {
			border: 2px solid white;
		}'''
