
var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue.js!'
  }
})

var app2 = new Vue({
  el: '#app-2',
  data: {
    message: 'You loaded this page on ' + new Date().toLocaleString()
  }
})

var app3 = new Vue({
  el: '#app-3',
  data: {
    seen: true
  },
  methods: {
    hideMessage: function () {
      this.seen = !this.seen
    }
  }
})

var app4 = new Vue({
  el: '#app-4',
  data: {
    todos: [
      { text: 'Learn JavaScript' },
      { text: 'Learn Vue' },
      { text: 'Build something awesome' }
    ]
  },
  methods: {
    newItem: function () {
      this.todos.push({ text: 'New item' })
    }
  }
})

var app5 = new Vue({
  el: '#app-5',
  data: {
    message: 'Hello Vue.js!'
  },
  methods: {
    reverseMessage: function () {
      this.message = this.message.split('').reverse().join('')
    }
  }

})

var app6 = new Vue({
  el: '#app-6',
  data: {
    message: 'Hello Vue.js!'
  }
})

// Define a new component called todo-item
Vue.component('todo-item', {
  props: ['todo'],
  template: '<li>{{ todo.text }}</li>'
})

var app7 = new Vue({
  el: '#app-7',
  data: {
    groceryList: [
      { id: 0, text: 'Vegetables' },
      { id: 1, text: 'Cheese' },
      { id: 2, text: 'Whatever else humans are supposed to eat' }
    ]
  }
})


var homepage = new Vue({
  el: '#homepage',
  data: {
    myApiData: 'mounting...'
  },
  methods: {
        fetchData: function () {
        this.myApiData = 'fetching';
            this.$http.get('/api/data/kazam')
                .then(function (response) {
                    this.myApiData = response.data.apiData;
                }, function (err) {
                    console.log(err);
                });
        }
    },
    mounted: function () {
        this.myApiData = 'fetching...';
        this.fetchData();
    }
})