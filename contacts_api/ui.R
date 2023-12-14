library(shiny)
shinyUI(
  fluidPage(
    titlePanel("Contacts"),
    sidebarLayout(
      sidebarPanel(
        textInput(
          inputId="first_name",
          label="First Name"
        ),
        textInput(
          inputId="last_name",
          label="Last Name"
        ),
        radioButtons(
          inputId="no_contact",
          label="Contact this person",
          choices=c('TRUE','FALSE'),
          selected="TRUE"
        ),
        selectInput(
          inputId = "role",
          label="Contact Role",
          choices=c(
            "Active Admin",
            "Active Industry",
            "Active Support",
            "Data User",
            "Inactive",
            "Unknown"
          ),
          multiple = FALSE,
          selectize = TRUE,
          selected = "Unknown"
        ),
        textInput(
          inputId='phone',
          label="Phone Number",
          placeholder="**********"
        ),
        textInput(
          inputId='email',
          label="email address",
          placeholder="name@website.com"
        ),
        textInput(
          inputId='address1',
          label="Street Address 1",
          placeholder="166 Water Street"
        ),
        textInput(
          inputId="address2",
          label="Street Address 2",
          placeholder="Suite 123"
        ),
        textInput(
          inputId="city",
          label="City",
          placeholder="Woods Hole"
        ),
        selectInput(
          inputId = "state",
          label="State",
          choices=c("CT","DE","MA","MD","ME","NC","NH","NJ","NY","PA","RI","SC","VT"),
          multiple = FALSE,
          selectize = TRUE,
          selected = "MA"
        ),
        textInput(
          inputId="zip",
          label="Zip Code",
          placeholder="01234"
        ),
        actionButton(
          inputId="submit",
          label="Submit"
        )
      ),
      mainPanel(
        textOutput(
          outputId="contact_json"
        )
      )
    )
  )
)