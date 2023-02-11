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
      <Title>DevOps Dashboard</Title>

      <Table
        title="Servers"
        task="view_aws_servers"
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