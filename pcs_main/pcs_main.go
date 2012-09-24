package index

import (
//	"appengine"
//	"appengine/urlfetch"
	"fmt"
	"html/template"
	"net/http"
)

const deploy = false;

var main_template string

type pcs_main_data struct {
	BandDescr   string
	DanielDescr string
}

func init() {
	http.HandleFunc("/", handler)
}
	
func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Hello")
	d := pcs_main_data{
		BandDescr: `
The Pie Crust Shell is a Progressive Rock group that kicks serious ass.
`,
		DanielDescr: `
Daniel Gonzalez is a cool dude and a fucking awesome musician.
			      He currently lives in Boston and is a student at Berklee.
`}
	t, err := template.ParseFiles("tmpl/pcs_main.html")
	if err != nil {
		panic(err)
	}
	t.Execute(w, d)
}
