<template>
  <nav class="navbar navbar-expand-md navbar-light fixed bg-success">
      <div class="container-fluid">
          <div class="card" style="width: 100%; margin: 0.75rem;">
              <a class="navbar-brand">
                  <h4>Personal Journal &#128077;</h4>
              </a>
              <hr>
              <h6 class="card-subtitle text-muted" style="font-size: 0.8rem;">Made by Rezwan</h6>
          </div>
      </div>
      <div class="container-fluid">
          <div class="card" style="width: 100%; margin: 0.75rem;">
              <a class="navbar-brand">
                  <h4>What to include in a journal?</h4>
              </a>
              <hr>
              <h6 class="card-subtitle text-muted" style="font-size: 0.8rem;">The highlights of your day, goals, quotes</h6>
          </div>
      </div>
    </nav>

  <body>
    <div>
        <div class="card" style="width: auto; background-color: #D1E7DD;">
            <table class="table table-danger, border border-2 border border-dark">
                <thead>
                    <tr>
                        <th class="bg-danger" scope="col">Journal Entries</th>
                    </tr>
                </thead>
                <tbody class="table-group-divider">
                    <!-- Displaying existing journal posts -->
                    <span v-for="collection in jPosts">
                        <tr v-for="instance in collection">
                            <th>{{instance.id}}</th>
                            <strong>Entry Title:</strong> 
                            <td>{{instance.journalheader}}</td>
                            <strong>Mood Rating:</strong> 
                            <td>{{instance.journalmoodrating}}</td>
                            <strong>Entry Content:</strong> 
                            <td>{{instance.journalcontent}}</td>
                            <strong>Daily Water Intake:</strong> 
                            <td>{{instance.journaldailywaterintake}}</td>
                            <strong>5 A Day:</strong> 
                            <td>{{instance.journaldailyfruits}}</td>
                            <strong>Last Modified:</strong> 
                            <td>{{instance.lastmodified}}</td>
                            <td><button class="btn btn-warning" type="button" @click="edit_journal(instance.id, instance.journalheader, instance.journalmoodrating, instance.journalcontent)" data-bs-toggle="modal" data-bs-target="#editPost">{{ instance.id }} - edit</button></td>
                            <td><button class="btn btn-info" type="button" @click="delete_journal(instance.id)">{{ instance.id }} - delete</button></td>
                        </tr>
                        <!-- Modal for editing existing journal post -->
                        <div class="modal fade" id="editPost" tabindex="-1" aria-hidden="true">
                            <div class="modal-dialog">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h5 class="modal-title">Edit journal </h5>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body">
                                        <form class="Edit-Post-Form">
                                            <div class="input-group">
                                                <span class="input-group-text">Entry Title:</span><input type="text" id="update-journal-title" class="form-control">
                                            </div>
                                            <hr>
                                            <div class="input-group">
                                                <span class="input-group-text">Mood Rating:</span>
                                                <select id="update-mood-rating" class="form-select" aria-label="Default select example">
                                                    <option value="1">1 - Terrible!</option>
                                                    <option value="2">2</option>
                                                    <option value="3">3</option>
                                                    <option value="4">4</option>
                                                    <option value="5">5 - Okay</option>
                                                    <option value="6">6</option>
                                                    <option value="7">7</option>
                                                    <option value="8">8</option>
                                                    <option value="9">9</option>
                                                    <option selected value="10">10 - Great!</option>
                                                </select>
                                            </div>
                                            <hr>
                                            <div class="input-group">
                                                <span class="input-group-text">Entry Content:</span>
                                                <textarea id='update-EntryContent' class="form-control" aria-label="With textarea"></textarea>
                                            </div>
                                            <hr>
                                            <div class="card">
                                                <div class="form-check form-switch">
                                                    <input class="form-check-input" type="checkbox" value = 'False' id="update-dailyWater">
                                                    <label class="form-check-label">Had Daily Water Intake (2.0 Litres)</label>
                                                </div>
                                            </div>
                                            <hr>
                                            <div class="card">
                                                <div class="form-check form-switch">
                                                    <input class="form-check-input" type="checkbox" value = 'False' id="update-dailyFruits">
                                                    <label class="form-check-label">Had 5 A Day - Enough Portions of Fruit and Vegetables</label>
                                                </div>
                                            </div>
                                            <hr>
                                        </form>
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                        <button type="button" data-bs-dismiss="modal" id="saveChanges" class="btn btn-primary">Save changes</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </span>
                </tbody>
            </table>
            <hr>            
            <button type="button" class="btn btn-primary" @click ="fetch_journal_posts">Get Journal Posts</button>
        </div>
        <div class="card bg-success">
            <!-- Main form for creating journal posts -->
            <form class="Add-Post-Form" @submit.prevent="post">
                <label class="form-label text-light">Fill in form to add a Journal Entry</label>
                <div class="input-group">
                    <span class="input-group-text">Entry Title:</span><input type="text" name = 'journalheader' id="journal-title" class="form-control" placeholder="The title of your journal post">
                </div>
                <hr>
                <div class="input-group">
                    <span class="input-group-text">Mood Rating:</span>
                    <select id="mood-rating" class="form-select" aria-label="Default select example">
                        <option value="1">1 - Terrible!</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5 - Okay</option>
                        <option value="6">6</option>
                        <option value="7">7</option>
                        <option value="8">8</option>
                        <option value="9">9</option>
                        <option selected value="10">10 - Great!</option>
                    </select>
                </div>
                <hr>
                <div class="input-group">
                    <span class="input-group-text">Entry Content:</span>
                    <textarea id='EntryContent' class="form-control" aria-label="With textarea" placeholder="Journal post content"></textarea>
                </div>
                <hr>
                <div class="card">
                    <div class="form-check form-switch">
                        <input class="form-check-input" type="checkbox" value = 'False' id="dailyWater">
                        <label class="form-check-label">Had Daily Water Intake (2.0 Litres)</label>
                    </div>
                </div>
                <hr>
                <div class="card">
                    <div class="form-check form-switch">
                        <input class="form-check-input" type="checkbox" value = 'False' id="dailyFruits">
                        <label class="form-check-label" for="flexSwitchCheckDefault">Had 5 A Day - Enough Portions of Fruit and Vegetables</label>
                    </div>
                </div>
                <hr>
                <button type="submit" @click ='fetch_journal_posts' class="btn btn-primary">Post Journal Entry</button>
            </form>
        </div>
    </div>
</body>
</template>

<script>
export default {
  async created(){
      await this.fetch_journal_posts()
  },
  data(){
    return {
      // jPosts - contains journal posts and is read when displayed in table-like format
      jPosts:[],
    }
  },
  methods: {
  async fetch_journal_posts(){
      fetch('http://localhost:8000/api/journals/', {method: "GET", headers: {
      "X-Requested-With": "XMLHttpRequest",}})
      .then((response) => response.json())
      .then((data) => this.jPosts=(data))
  },
  async post(){ 
    await this.fetch_journal_posts();  
      const titleValue = document.getElementById('journal-title')        
      const moodValue = document.getElementById('mood-rating')        
      const contentValue = document.getElementById('EntryContent')                
      var waterIntake = 'False';
      if (document.getElementById('dailyWater').checked) {
          waterIntake = 'True';
      }
      var fruitsEaten = 'False';
      if (document.getElementById('dailyFruits').checked) {
          fruitsEaten = 'True';
      }
      fetch('http://localhost:8000/api/journals/', {
          method:'POST',
          credentials: 'include',
          headers: {
          'X-Requested-With': 'XMLHttpRequest',
          'Content-Type':'application/json'
          },
          body: JSON.stringify({
            journalheader: titleValue.value,
            journalmoodrating: moodValue.value,
            journalcontent: contentValue.value,
            dailyWaterIntake: waterIntake,
            dailyFruitsHad: fruitsEaten
          })
      }).then(response => response.json())   
      await this.fetch_journal_posts();       
  },
  async delete_journal(id){        
    await this.fetch_journal_posts();
      fetch( 'http://localhost:8000/api/journals/', {
          method:'DELETE',
          credentials: 'include',
          headers: {
          'X-Requested-With': 'XMLHttpRequest',
          'Content-Type':'application/json'
          },
          body: JSON.stringify({
            journalid:id
          })
      }).then(response=>response.json)
      await this.fetch_journal_posts();
  },
  async prepareUpdateForm(header, moodrating, content){
      // Adding existing journal entry's value to make easier editing a journal post
      document.getElementById('update-journal-title').value = header;        
      document.getElementById('update-mood-rating').value = moodrating;        
      document.getElementById('update-EntryContent').value = content;          
  },
  async edit_journal(id, header, moodrating, content){        
      await this.fetch_journal_posts();
      document.getElementById('update-journal-title').value = header;        
      document.getElementById('update-mood-rating').value = moodrating;        
      document.getElementById('update-EntryContent').value = content;

      const save_changes_button = document.getElementById('saveChanges');
      // default variable values that are soon changed
      var titleValue = 'title';
      var moodValue = 5;
      var contentValue = 'content';
      var waterIntake = 'False';
      var fruitsEaten = 'False';

      save_changes_button.addEventListener("click", () => {
      titleValue = document.getElementById('update-journal-title').value;        
      moodValue = document.getElementById('update-mood-rating').value;        
      contentValue = document.getElementById('update-EntryContent').value;                
          
      if (document.getElementById('update-dailyWater').checked) {
          waterIntake = 'True';
      }
      if (document.getElementById('update-dailyFruits').checked) {
          fruitsEaten = 'True';
      }
      fetch('http://localhost:8000/api/journals/', {
          method:'PUT',
          credentials: 'include',
          headers: {
          'X-Requested-With': 'XMLHttpRequest',
          'Content-Type':'application/json'
          },
          body: JSON.stringify({
            journalid:id, 
            journalheader: titleValue,
            journalmoodrating: moodValue,
            journalcontent: contentValue,
            dailyWaterIntake: waterIntake,
            dailyFruitsHad: fruitsEaten
          })
      }).then(response=>response.json) // <--- (?)
      this.fetch_journal_posts();
      });           
        await this.fetch_journal_posts();
        }    
    }, 
    mounted(){
    this.fetch_journal_posts();
    }
}
</script>

<style>
table {
  border-spacing: 1rem;
  border-width: 1rem;
}
td, tr, th {
  padding: 1rem;
  border: 1rem;
}
</style>