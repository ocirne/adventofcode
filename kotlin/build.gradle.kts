import org.jetbrains.kotlin.gradle.tasks.KotlinCompile

plugins {
    kotlin("jvm") version "1.4.31"
    id("org.cyclonedx.bom") version "1.7.3"
}

repositories {
    mavenCentral()
}

tasks.withType<KotlinCompile>().configureEach {
    kotlinOptions {
        jvmTarget = "11"
    }
}

tasks.withType<Test> {
    useJUnitPlatform()
}

dependencies {
    implementation(kotlin("stdlib"))

    testImplementation(platform("org.junit:junit-bom:5.7.1"))
    testImplementation("org.junit.jupiter:junit-jupiter")
    testImplementation("io.kotest:kotest-runner-junit5:4.4.1")
    testImplementation("io.kotest:kotest-assertions-core:4.4.1")
    testImplementation("com.opencsv:opencsv:5.4")
    testImplementation("org.jetbrains.kotlin:kotlin-reflect:1.4.31")
    testImplementation("org.reflections:reflections:0.9.12")
}

configurations {
    implementation {
        resolutionStrategy.failOnVersionConflict()
    }
}

configure<JavaPluginConvention> {
    sourceCompatibility = JavaVersion.VERSION_11
    targetCompatibility = JavaVersion.VERSION_11
}

tasks {
    test {
        testLogging.showExceptions = true
    }
}

tasks.cyclonedxBom {
    setIncludeConfigs(listOf("runtimeClasspath"))
    setProjectType("application")
    setSchemaVersion("1.4")
    setDestination(project.file("build/reports"))
    setOutputName("bom")
    setOutputFormat("json")
    setIncludeBomSerialNumber(false)
}
