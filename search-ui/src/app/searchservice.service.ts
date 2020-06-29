import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {map} from "rxjs/operators";


@Injectable({
  providedIn: 'root'
})

export class SearchserviceService {

  constructor(protected http: HttpClient) { }

  public get(searchTerm: string) {
    return this.http.get<Result>("http://localhost:8983/solr/songs_final/select",{
      params : {
        q : searchTerm,
        rows : '700'
      }
    })
      .pipe(
        map(results => results)
      );
  }

  public getTopSongs() {
    return this.http.get<Result>("http://localhost:8983/solr/songs_final/select",{
      params : {
        q : '*',
        sort : 'visits desc',
        rows : '700'
      }
    })
      .pipe(
        map(results => results)
      );
  }

  public getArtist(searchTerm : string) {
    return this.http.get<Result>("http://localhost:8983/solr/songs_final/select",{
      params : {
        q : 'artist : '.concat(searchTerm),
        rows : '700'
      }
    })
      .pipe(
        map(results => results)
      );
  }

  public getMusic(searchTerm : string) {
    return this.http.get<Result>("http://localhost:8983/solr/songs_final/select",{
      params : {
        q : 'music : '.concat(searchTerm),
        rows : '700'
      }
    })
      .pipe(
        map(results => results)
      );
  }

  public getLyricsBy(searchTerm : string) {
    return this.http.get<Result>("http://localhost:8983/solr/songs_final/select",{
      params : {
        q : 'lyrics_by : '.concat(searchTerm),
        rows : '700'
      }
    })
      .pipe(
        map(results => results)
      );
  }

  public getGreaterThanVisits(searchTerm : string) {
    return this.http.get<Result>("http://localhost:8983/solr/songs_final/select",{
      params : {
        q : 'visits : ['+searchTerm+' TO *]',
        sort : 'visits asc',
        rows : '700'
      }
    })
      .pipe(
        map(results => results)
      );
  }

  public getLowerThanVisits(searchTerm : string) {
    return this.http.get<Result>("http://localhost:8983/solr/songs_final/select",{
      params : {
        q : 'visits : [ * TO '+searchTerm+']',
        sort : 'visits asc',
        rows : '700'
      }
    })
      .pipe(
        map(results => results)
      );
  }

}

export interface Doc {
  artist : string;
  lyrics : string;
  name : string;
  genre : string;
  lyrics_by : string;
  visits : string;
  key : string;
  beat : string;
  music : string;
}

export interface Response {
  docs : Doc[];
}

export  interface Result {
  response : Response,
  responseHeader : any
}
