
package ${obj.component.package_name()}.controller;

import java.util.List;
import java.util.Map;

import javax.servlet.http.HttpServletRequest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Scope;
import org.springframework.data.domain.Page;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import ${obj.component.package_name()}.entity.${obj.name};
import ${obj.component.package_name()}.service.${obj.name}Service;
import com.faceye.feature.controller.BaseController;
import com.faceye.feature.util.http.HttpUtil;

@Controller
@Scope("prototype")
@RequestMapping("/${obj.component.name}/${obj.get_lower_start_clazz_name()}")
public class ${obj.name}Controller extends BaseController<${obj.name}, Long, ${obj.name}Service> {

	@Autowired
	public ${obj.name}Controller(${obj.name}Service service) {
		super(service);
	}
}