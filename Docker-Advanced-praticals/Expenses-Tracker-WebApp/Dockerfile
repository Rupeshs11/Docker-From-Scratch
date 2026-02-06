#stage-1 - BUild the JAR (java application Runtime) using maven
FROM maven:3.9.12-eclipse-temurin-17 AS builder

WORKDIR /app

COPY . .

RUN apt-get update && \
    apt-get install -y ca-certificates && \
    update-ca-certificates

RUN mvn clean install -DskipTests=true \
    -Dmaven.wagon.http.ssl.protocols=TLSv1.2

#stage 2 - Execute JAR Files from the above stage

FROM eclipse-temurin:17-jdk-alpine

WORKDIR /app

COPY --from=builder /app/target/*.jar expenseapp.jar

CMD ["java","-jar","expenseapp.jar"]
