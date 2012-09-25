package index

import (
//	"appengine"
//	"appengine/urlfetch"
	"fmt"
	"html/template"
	"net/http"
)

func init() {
	http.HandleFunc("/", handler)
}
	
func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Hello")
	t, err := template.ParseFiles("tmpl/pcs_main.html")
	if err != nil {
		panic(err)
	}
	t.Execute(w, nil)
}
