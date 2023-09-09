def tech ():
    raw = "Python, Java, JavaScript, C++, C#, Ruby, Go, Swift, Kotlin, PHP, Rust, TypeScript, HTML/CSS, SQL, Shell scripting (Bash), MATLAB, R, Scala, Perl, Objective-C, Groovy, Lua, Dart, Julia, Haskell, PowerShell, Groovy, VB.NET, COBOL, Fortran, Ada, Lisp, Prolog, Scheme, Tcl, Delphi, F#, Elixir, Erlang, PL/SQL, SAS, Crystal, CoffeeScript, Django, Flask, Spring, Node.js, React, Angular, Vue.js, Ruby on Rails, ASP.NET, Laravel, Express.js, HTML5, CSS3, Bootstrap, Sass, Less, jQuery, Ember.js, Backbone.js, D3.js, Flask, Redux, RESTful API, GraphQL, Firebase, Android Development, iOS Development, React Native, Flutter, Xamarin, Ionic, Swift, Objective-C, Kotlin, Java, PhoneGap, Cordova, Mobile UI/UX, TensorFlow, PyTorch, scikit-learn, Keras, NumPy, Pandas, R, MATLAB, Apache Spark, Hadoop, SQL, Data Mining, Natural Language Processing (NLP), Deep Learning, Reinforcement Learning, Computer Vision, Big Data Analytics, Kubernetes, Docker, AWS (Amazon Web Services), Azure (Microsoft Cloud), Google Cloud Platform (GCP), Ansible, Jenkins, Puppet, Chef, Terraform, Git, CI/CD, Serverless Architecture, Microservices, Infrastructure as Code (IaC), MySQL, PostgreSQL, MongoDB, Oracle, SQL Server, SQLite, Redis, Firebase, Elasticsearch, Apache Kafka, GraphQL, RESTful API, Node.js, Django, Flask, Express.js, Ruby on Rails, Git, Linux, Bash, Windows, Networking, Security, Artificial Intelligence (AI), Blockchain, Cryptography, Virtual Reality (VR), Augmented Reality (AR), Internet of Things (IoT), Game Development"
    lst = raw.split(", ")
    formatted = ','.join(lst)
    print(formatted)

def main ():
    raw = "210.0,40%,185.0,105.0,90%,220.0,195.0,75%,270.0,155.0,85.0,155.0%,10.0,230%,150.0,235.0,35%,285.0,260.0,100%,80%,60.0,150%,20.0,290.0,185.0,50%,90.0,100%,130%,235.0,170.0,30%,185.0,185.0,210.0,30%,190.0,60%,225.0,275.0,210.0,190.0,20.0,140%,110%,220.0,280.0,155.0%,70%,295.0,110%,245.0,5.0,295.0,55%,115%,80%,80.0,20.0,85%,55%,270.0,200.0,40%,170.0,190.0,265.0,55%,190.0,40%,270.0,275.0,25%,110%,260.0,160.0,40%,220.0,125%,40%,295.0,135%,40%,210.0,235.0,255.0,190.0,270.0,235.0,195.0,125%,170.0,270.0,195.0,50%,185.0,70%,160.0,140%,205.0,15.0,85%,215.0,55%,5.0,230.0,170%,285.0,25.0,40%,190.0,200.0,55%,270.0,125%,145%,220.0,75%,155%,80.0,225.0,40%,70%,180.0,150%,230.0,275.0,10.0,15.0,240.0,165.0,55%,65.0,15.0,200.0,125%,180.0,190.0,270.0,195%,70.0,20.0,150%,175.0,270.0,80%,150%,220.0,35%,125%,95%,280.0,150%,125%,175%,140.0,205%,120%,145.0,165.0,35%,275.0,25%,160.0,220.0,105.0,40%,110%,85.0,235.0,70%,10.0,130%,230.0,120%,190.0,105"
    
    formatted = ""
    for c in raw:
        if c == '%': formatted += "\%"
        else: formatted += c
    print(formatted)

if __name__=="__main__":
    main()