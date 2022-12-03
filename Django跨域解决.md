# 在setting文件中修改：

来自：https://www.bilibili.com/video/BV17L4y1a78L/?spm_id_from=333.337.search-card.all.click&vd_source=7f36373aadbc43bdc33f570e030222b0



Django 实现跨域
pip install django-cors-headers

后端django根目录settings.py
INSTALLED_APPS = [
		...
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', // 跨域设置
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
添加
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = ('*')

​    // //mac版本直接采用axios方式发送post请求，会出现跨域问题

​    // axios({

​    //   url: 'http://127.0.0.1:3000/tbridge/t/',

​    //   method: 'post',

​    //   data: {

​    //     task_name: 'trainify_verify',

​    //   },

​    // }).then((res) => {

​    //   console.log(res);

​    // });