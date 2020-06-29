import { Component, OnInit } from '@angular/core';
import {SearchserviceService,Doc} from "../searchservice.service";

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})

export class SearchComponent implements OnInit {

  query : ''
  results : Doc [];

  constructor(public searchservice : SearchserviceService ) { 
    this.query = ''
    this.results = []
  }

  ngOnInit(): void {
  }

  istopsongs(query) {
    let arr = ['හොදම','ජනප්‍රියම','ජනප්‍රිය','හොන්දම','හොද','හොඳම​']
    for (var i=0 ; i< arr.length ; i++) {
      if (query.includes(arr[i].trim())) {
        return true;
      } 
    }
    return false
  }

  isArtist(query){
    let arr = ['ගැයූ','කියපු','ගායනා']
    for (var i=0 ; i< arr.length ; i++) {
      if (query.includes(arr[i].trim())) {
        return true;
      } 
    }
    return false
  }

  isMusic(query){
    let arr = ['සංගීතවත්','සංගීතය','වාදනය']
    for (var i=0 ; i< arr.length ; i++) {
      if (query.includes(arr[i].trim())) {
        return true;
      } 
    }
    return false
  }

  isLyricsBy(query){
    let arr = ['ලියූ','ලියන','ලියපු','රචනා','පදරචනය']
    for (var i=0 ; i< arr.length ; i++) {
      if (query.includes(arr[i].trim())) {
        return true;
      } 
    }
    return false
  }

  isgreaterthanvisits(query : string){
    let lst = query.split(' ')
    
    let arr = ['ඉක්මවූ','වැඩි','ඉක්මවා','වැඩියෙන්','ඉහල','ඉහළ']
    for (var i=0 ; i< lst.length ; i++) {
      if (arr.indexOf(lst[i].trim()) != -1 )
      {
        if (query.match(/\d+/) != null) {
          return true
        }
      } 
    }
    return false
  }

  islowerthanvisits(query : string){
    let lst = query.split(' ')
    let arr = ['නොයික්මවු','නොයික්මවූ','අඩු','පහල','පහළ']
    for (var i=0 ; i< lst.length ; i++) {
      if (arr.indexOf(lst[i].trim()) != -1 )
      {
        if (query.match(/\d+/) != null) {
          return true
        }
      } 
    }
    return false
  }



  public getResult() {

    let all = "සියලුම ගීත​"
    if (this.query.trim() == all ) {

      this.searchservice.get("*").subscribe((result) => {
        this.results = result.response.docs;
      })

    } else if (this.isgreaterthanvisits(<string>this.query)){
      let number = this.query.match(/\d+/)[0]
      
      this.searchservice.getGreaterThanVisits(number).subscribe((result) => {
        this.results = result.response.docs;
      })


    } else if (this.islowerthanvisits(<string>this.query)){
      let number = this.query.match(/\d+/)[0]
      
      this.searchservice.getLowerThanVisits(number).subscribe((result) => {
        this.results = result.response.docs;
      })
    } else if (this.istopsongs(this.query)) {

      this.searchservice.getTopSongs().subscribe((result) => {
        this.results = result.response.docs;
      })

    } else if (this.isArtist(this.query)) {

      let query = <string>this.query
      let arr = ['ගැයූ','කියපු','ගායනා','කල','කළ','ගීත','සිංදු']
      for (var i=0 ; i< arr.length ; i++) {
        query = query.replace(arr[i],'')
      }
      this.searchservice.getArtist(query).subscribe((result) => {
        this.results = result.response.docs;
      })

    } else if (this.isMusic(this.query)) {

      let query = <string>this.query
      let arr = ['සංගීතවත්','සංගීතය','වාදනය','කල','කළ','ගීත','සිංදු','සැපයූ']
      for (var i=0 ; i< arr.length ; i++) {
        query = query.replace(arr[i],'')
      }
      this.searchservice.getMusic(query).subscribe((result) => {
        this.results = result.response.docs;
      })

    } else if (this.isLyricsBy(this.query)) {

      let query = <string>this.query
      let arr = ['ලියූ','ලියන','ලියපු','රචනා','පදරචනය','කල','කළ','ගීත','සිංදු']
      for (var i=0 ; i< arr.length ; i++) {
        query = query.replace(arr[i],'')
      }
      this.searchservice.getLyricsBy(query).subscribe((result) => {
        this.results = result.response.docs;
      })

    } else {
      
      // සිංදු ගීත අයින් කරන්න query yawanna kalin

      this.searchservice.get(this.query).subscribe((result) => {
        this.results = result.response.docs;
      })
    }

  }

  
}