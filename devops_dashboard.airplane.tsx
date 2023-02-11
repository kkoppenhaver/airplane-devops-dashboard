import {
  Stack,
  Table,
  Title,
  useComponentState,
  Card,
  Text,
  Button,
} from "@airplane/views";
import airplane from "airplane";

// Views documentation: https://docs.airplane.dev/views/getting-started
const DevOpsDashboard = () => {
  return (
    <Stack>
      <Stack direction="row">
        <Title>DevOps Dashboard</Title>
        <Button variant="light" id="createButton" task={{ slug: "create_aws_servers" }}>
          Create Server
        </Button>
      </Stack>

      <Table
        title="Servers"
        task="view_aws_servers"
        rowActions={[
          {
            slug: "delete_aws_servers", 
            label: "Delete Server",
            rowTransform: (row) => ({
              instance_id: row.ID,
            }),
          }
        ]}
      />
    </Stack>
  );
};

export default airplane.view(
  {
    slug: "devops_dashboard",
    name: "DevOps Dashboard",
  },
  DevOpsDashboard
);