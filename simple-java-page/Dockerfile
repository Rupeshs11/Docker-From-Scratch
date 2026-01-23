# pulling the base image which gives all the required tools and Libraries
FROM eclipse-temurin:17-jdk-alpine

# create a folder where the app code will be stored
WORKDIR /app

# Copy the source code form host machine to the conatainer
COPY src/Main.java ./Main.java

# Compile the application code
RUN javac Main.java

# run the application
CMD ["java","Main"]




