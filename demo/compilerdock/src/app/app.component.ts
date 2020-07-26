import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'compiler';
  editorOptions = {theme: 'vs-dark', language: 'javascript'};
  code: string= '';

  constructor(private http: HttpClient){}
  stdout:string;
  submit(){
    var e=<HTMLSelectElement>document.getElementById('lang');
    var lang = e.options[e.selectedIndex].value;
    var stdin = <HTMLTextAreaElement>document.getElementById('stdin-text');
    var payload={
      lang: lang,
      code: this.code,
      id: "1",
      stdin: stdin.value
    };

    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json'
      })
    };
    this.http.post('http://localhost:5000/',payload,httpOptions).subscribe((res:any)=>{
      this.stdout=res.output;
      document.getElementById('stdout-text').innerText=this.stdout;
    });

  }
}
