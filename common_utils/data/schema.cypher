CREATE NODE TABLE User(name STRING, age INT64, PRIMARY KEY (name))
CREATE NODE TABLE City(name STRING, population INT64, PRIMARY KEY (name))
CREATE REL TABLE Follows(FROM User TO User, since INT64)
CREATE REL TABLE LivesIn(FROM User TO City)