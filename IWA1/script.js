      fetch("https://api.github.com/users/aaganmaskey")
        .then((response) => response.json())
        .then(function (data) {
          //console.log(data)

          let followersCount = data["followers"];
          let followersInfo = `I have been followed by ${followersCount} awesome people on GitHub`;

          document.getElementById("profileImage").src = data["avatar_url"];
          document.getElementById("fullName").textContent = data["name"];
          document.getElementById("bioInfo").textContent = data["bio"];
          document.getElementById("twitterHandle").textContent = data["twitter_username"];
          document.getElementById("followersInfo").textContent = followersInfo;
          document.getElementById("githubLink").href = data["html_url"];
        });
      fetch("https://api.github.com/users/aaganmaskey/repos")
        .then((response) => response.json())
        .then((repos) => {
          repos.forEach((repo) => {
            linebreak = document.createElement("br");
            // sdocument.getElementById("repos").append(`${repo.id}`);
            document.getElementById("repos").append(`${repo.name}`);
            // document.getElementById("repos").append(`${repo.html_url}`);
            document.getElementById("repos").append(linebreak);
          });
        });