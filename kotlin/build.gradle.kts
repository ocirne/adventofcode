import org.jetbrains.kotlin.gradle.dsl.JvmTarget

plugins {
    kotlin("jvm") version "2.1.0"
}

repositories {
    mavenCentral()
}

kotlin {
    jvmToolchain(17)
    compilerOptions {
        jvmTarget.set(JvmTarget.JVM_17)
    }
}

tasks.withType<Test> {
    useJUnitPlatform()
    testLogging.showExceptions = true
}

dependencies {
    implementation(kotlin("stdlib"))

    testImplementation(platform("org.junit:junit-bom:5.11.4"))
    testImplementation("org.junit.jupiter:junit-jupiter")
    testImplementation("io.kotest:kotest-runner-junit5:5.9.1")
    testImplementation("io.kotest:kotest-assertions-core:5.9.1")
    testImplementation("com.opencsv:opencsv:5.9")
    testImplementation("org.jetbrains.kotlin:kotlin-reflect:2.1.0")
    testImplementation("org.reflections:reflections:0.10.2")
}

configurations {
    implementation {
        resolutionStrategy.failOnVersionConflict()
    }
}
